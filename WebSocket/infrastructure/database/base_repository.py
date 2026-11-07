import logging

from infrastructure.database.connection import get_connection
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult

logger = logging.getLogger(__name__)

class BaseRepository:
    #Metodo para ejecutar POST (INSERT) o PUT (UPDATE)
    @staticmethod
    def execute_operation(query: str, params: tuple = ()) -> OperationResult:
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)

                while cursor.description is None:
                    if not cursor.nextset():
                        return OperationResult(
                            status_code=500,
                            message_user="No se recibió respuesta del procedimiento almacenado.",
                            message_tech="El procedimiento no devolvió un resultset."
                        )
                result = cursor.fetchone()
                conn.commit()

                if result is None:
                    return OperationResult(
                        status_code=500,
                        message_user="No se recibió respuesta del procedimiento almacenado.",
                        message_tech="fetchone() retornó None."
                    )

                return OperationResult(
                    status_code=result[0],
                    message_user=result[1],
                    message_tech=result[2]
                )

        except Exception:
            logger.exception("Database operation failed")
            return OperationResult(
                status_code=500,
                message_user="No fue posible completar la operación.",
                message_tech=None
            )
        
    #Metodo para ejecutar GET (SELECT)
    @staticmethod
    def execute_query(
        query: str,
        params: tuple = ()
    ) -> QueryResult:

        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)

                while cursor.description is None:
                    if not cursor.nextset():
                        return QueryResult(
                            status_code=500,
                            message_user="No se recibieron resultados del procedimiento almacenado.",
                            message_tech="El procedimiento no devolvió un resultset.",
                            data=[]
                        )
                columns = [col[0] for col in cursor.description]
                data = [
                    dict(zip(columns, row))
                    for row in cursor.fetchall()
                ]

                while cursor.nextset():
                    if cursor.description is not None:
                        operation = cursor.fetchone()
                        return QueryResult(
                            status_code=operation[0],
                            message_user=operation[1],
                            message_tech=operation[2],
                            data=data
                        )

                return QueryResult(
                    status_code=500,
                    message_user="No se recibieron parámetros de salida.",
                    message_tech="El procedimiento no retornó un segundo resultset.",
                    data=data
                )

        except Exception:
            logger.exception("Database query failed")
            return QueryResult(
                status_code=500,
                message_user="No fue posible consultar la información.",
                message_tech=None,
                data=[]
            )


class StoredProcedureRepository(BaseRepository):
    """Base para repositorios que ejecutan procedimientos con parámetros nombrados."""

    SP_NAME: str

    def execute_procedure(self, action: str, params: dict[str, object], *, query: bool = False):
        assignments = ",\n                ".join(
            f"@{name} = ?" for name in params
        )
        sql = f"""
            DECLARE @o_Numero INT;
            DECLARE @o_MensajeTecnico VARCHAR(500);
            DECLARE @o_MensajeUsuario VARCHAR(500);

            EXEC {self.SP_NAME}
                {assignments},
                @w_Accion = ?,
                @o_Numero = @o_Numero OUTPUT,
                @o_MensajeTecnico = @o_MensajeTecnico OUTPUT,
                @o_MensajeUsuario = @o_MensajeUsuario OUTPUT;

            SELECT
                @o_Numero AS status_code,
                @o_MensajeUsuario AS message_user,
                @o_MensajeTecnico AS message_tech;
        """
        values = (*params.values(), action)

        if query:
            return self.execute_query(sql, values)
        return self.execute_operation(sql, values)
