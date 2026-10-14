USE [DB_SCRUM_PLANNING]
GO

CREATE OR ALTER PROC [SQM_CATALOGS].[USP_Status]
(
    @i_statusId INT = NULL,
    @i_statusName VARCHAR(80) = NULL,
    @i_statusCreationDate DATETIME = NULL,
    @i_statusCreatorId INT = NULL,
    @i_statusModificationDate DATETIME = NULL,
    @i_statusModificatorId INT = NULL,
    @i_statusEnable BIT = NULL,
    @i_PageNumber INT = NULL,
    @i_RowsPerPage INT = NULL,
    @w_Accion CHAR(1),
    @o_Numero INT = NULL OUT,
    @o_MensajeTecnico VARCHAR(500) = NULL OUT,
    @o_MensajeUsuario VARCHAR(500) = NULL OUT
)

AS
BEGIN

    DECLARE @w_totalRows INT;

    IF @i_statusCreationDate IS NULL
        SET @i_statusCreationDate = GETDATE();

    IF @i_statusModificationDate IS NULL
        SET @i_statusModificationDate = GETDATE();

    -- INSERTAR STATUS --
    IF @w_Accion = 'I'
    BEGIN
        IF ISNULL(@i_statusName,'') = ''
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL NOMBRE DEL ESTADO ES OBLIGATORIO';
        END;

        ELSE
        BEGIN
            INSERT INTO [SQM_CATALOGS].[TBL_Status] (statusName,statusCreationDate,statusCreatorId,statusModificationDate,statusModificatorId,statusEnable)
            VALUES(@i_statusName,@i_statusCreationDate,@i_statusCreatorId,@i_statusModificationDate,@i_statusModificatorId,@i_statusEnable);
            SET @o_Numero = 201;
            SET @o_MensajeUsuario = 'ESTADO CREADO EXITOSAMENTE';
        END;
    END;

    -- UPDATE STATUS --
    ELSE IF @w_Accion = 'U'
    BEGIN
        IF ISNULL(@i_statusId,0) = 0
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL ID DEL ESTADO ES OBLIGATORIO';
        END;

        ELSE IF NOT EXISTS (SELECT 1 FROM [SQM_CATALOGS].[TBL_Status] (NOLOCK) WHERE statusId = @i_statusId)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'EL ESTADO NO EXISTE';
        END;

        ELSE IF ISNULL(@i_statusName,'') = ''
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL NOMBRE DEL ESTADO ES OBLIGATORIO';
        END;

        ELSE IF ISNULL(@i_statusModificatorId,0) = 0
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL ID DEL MODIFICADOR ES OBLIGATORIO';
        END;

        ELSE IF NOT EXISTS (SELECT 1 FROM [SQM_SECURITY].[TBL_Users] (NOLOCK) WHERE userId = @i_statusModificatorId AND userEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'EL MODIFICADOR NO EXISTE O NO ESTA HABILITADO';
        END;

        ELSE
        BEGIN
            UPDATE [SQM_CATALOGS].[TBL_Status]
            SET statusName = @i_statusName,
                statusModificationDate = @i_statusModificationDate,
                statusModificatorId = @i_statusModificatorId,
                statusEnable = @i_statusEnable
            WHERE statusId = @i_statusId;

            SET @o_Numero = 200;
            SET @o_MensajeUsuario = 'ESTADO ACTUALIZADO EXITOSAMENTE';
        END;
    END;

    -- SELECT STATUS --
    ELSE IF @w_Accion = 'S'
    BEGIN
        BEGIN TRY

        SELECT statusId,statusName,statusCreationDate,statusCreatorId,statusModificationDate,statusModificatorId,statusEnable
        FROM [SQM_CATALOGS].[TBL_Status] (NOLOCK)
        ORDER BY statusId
        OFFSET (@i_PageNumber - 1) * @i_RowsPerPage ROWS
        FETCH NEXT @i_RowsPerPage ROWS ONLY;

        SET @w_totalRows = @@ROWCOUNT;

        IF @w_totalRows > 0
        BEGIN
            SET @o_Numero = 200;
            SET @o_MensajeUsuario = 'ESTADOS OBTENIDOS EXITOSAMENTE';
        END
        ELSE
        BEGIN
            SET @o_Numero = 204;
            SET @o_MensajeUsuario = 'NO HAY MAS REGISTROS PARA LISTAR';
        END
        END TRY

        BEGIN CATCH
            SET @o_Numero = 500;
            SET @o_MensajeUsuario = 'ERROR AL OBTENER LOS ESTADOS';
            SET @o_MensajeTecnico = ERROR_MESSAGE();
        END CATCH
    END

    -- ACCIÓN INVÁLIDA --
    ELSE
    BEGIN
        SET @o_Numero = 400;
        SET @o_MensajeUsuario = 'ACCIÓN INVÁLIDA';
    END
END;
GO