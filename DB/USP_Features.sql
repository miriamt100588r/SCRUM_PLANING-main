USE [DB_SCRUM_PLANNING]
GO

CREATE OR ALTER PROC [SQM_GENERAL].[USP_Features]
(
    @i_featureId INT = NULL,
    @i_featureSummary VARCHAR(500) = NULL,
    @i_featureDescription VARCHAR(2000) = NULL,
    @i_featuresAcceptanceCriteria VARCHAR(4000) = NULL,
    @i_featureParentLink INT = NULL,
    @i_featureOwner INT = NULL,
    @i_featureStartDate DATE = NULL,
    @i_featureDueDate DATE = NULL,
    @i_featurePriority INT = NULL,
    @i_featureCreationDate DATETIME = NULL,
    @i_featureCreatorId INT = NULL,
    @i_featureModificationDate DATETIME = NULL,
    @i_featureModificatorId INT = NULL,
    @i_featureStatus INT = NULL,
    @i_PageNumber INT = NULL,
    @i_RowsPerPage INT = NULL,
    @w_Accion CHAR(1),
    @o_Numero INT = NULL OUT,
    @o_MensajeTecnico VARCHAR(500) = NULL OUT,
    @o_MensajeUsuario VARCHAR(500) = NULL OUT
)
AS
BEGIN

    DECLARE @w_totalRows INT, @w_featureStartDate DATE, @w_featureDueDate DATE;

    IF @i_featureCreationDate IS NULL
        SET @i_featureCreationDate = GETDATE();

    IF @i_featureModificationDate IS NULL
        SET @i_featureModificationDate = GETDATE();

    -- INSERTAR Feature --
    IF @w_Accion = 'I'
    BEGIN
        IF ISNULL(@i_featureSummary,'') = ''
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL RESUMEN ES OBLIGATORIO';
        END;

        ELSE IF ISNULL(@i_featureDescription,'') = ''
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'LA DESCRIPCION ES OBLIGATORIA';
        END;

        ELSE IF ISNULL(@i_featuresAcceptanceCriteria,'') = ''
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'LOS CRITERIOS DE ACEPTACION SON OBLIGATORIOS';
        END;

        ELSE IF ISNULL(@i_featureParentLink,0) = 0
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'LA EPICA PADRE ES OBLIGATORIA';
        END;

        ELSE IF ISNULL(@i_featureOwner,0) = 0
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL PROPIETARIO ES OBLIGATORIO';
        END;

        ELSE IF ISNULL(@i_featureStatus,0) = 0
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL ESTADO ES OBLIGATORIO';
        END;

        ELSE IF ISNULL(@i_featureCreatorId,0) = 0
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL ID DEL CREADOR ES OBLIGATORIO';
        END;

        ELSE IF NOT EXISTS (SELECT 1 FROM [SQM_SECURITY].[TBL_Users] (NOLOCK) WHERE userId = @i_featureCreatorId AND userEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'EL USUARIO CREADOR NO EXISTE O NO ESTA HABILITADO';
        END;

        ELSE IF NOT EXISTS (SELECT 1 FROM [SQM_GENERAL].[TBL_Epics] (NOLOCK) WHERE epicId = @i_featureParentLink)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'LA EPICA PADRE NO EXISTE';
        END;

        ELSE IF NOT EXISTS (SELECT 1 FROM [SQM_SECURITY].[TBL_Users] (NOLOCK) WHERE userId = @i_featureOwner AND userEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'EL PROPIETARIO NO EXISTE O NO ESTA HABILITADO';
        END;

        ELSE IF @i_featurePriority IS NOT NULL AND NOT EXISTS (SELECT 1 FROM [SQM_CATALOGS].[TBL_Priorities] (NOLOCK) WHERE priorityId = @i_featurePriority AND priorityEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'LA PRIORIDAD NO EXISTE O NO ESTA HABILITADA';
        END;

        ELSE IF NOT EXISTS (SELECT 1 FROM [SQM_CATALOGS].[TBL_Status] (NOLOCK) WHERE statusId = @i_featureStatus AND statusEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'EL ESTADO NO EXISTE O NO ESTA HABILITADO';
        END;

        ELSE IF @i_featureStartDate IS NOT NULL AND @i_featureDueDate IS NOT NULL AND @i_featureDueDate < @i_featureStartDate
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'LA FECHA LIMITE NO PUEDE SER MENOR A LA FECHA INICIAL';
        END;

        ELSE
        BEGIN
            BEGIN TRANSACTION TRX_INS_FEATURE;

            BEGIN TRY

                INSERT INTO [SQM_GENERAL].[TBL_Features](featureSummary,featureDescription,featuresAcceptanceCriteria,featureParentLink,featureOwner,featureStartDate,featureDueDate,featurePriority,featureCreationDate,featureCreatorId,featureModificationDate,featureStatus)
                VALUES(@i_featureSummary,@i_featureDescription,@i_featuresAcceptanceCriteria,@i_featureParentLink,@i_featureOwner,@i_featureStartDate,@i_featureDueDate,@i_featurePriority,@i_featureCreationDate,@i_featureCreatorId,@i_featureModificationDate,@i_featureStatus);

                COMMIT TRANSACTION TRX_INS_FEATURE;

                SET @o_Numero = 201;
                SET @o_MensajeUsuario = 'FUNCIONALIDAD REGISTRADA CORRECTAMENTE';

            END TRY

            BEGIN CATCH

                IF @@TRANCOUNT > 0
                    ROLLBACK TRANSACTION TRX_INS_FEATURE;

                SET @o_Numero = 500;
                SET @o_MensajeUsuario = 'ERROR AL REGISTRAR FUNCIONALIDAD';
                SET @o_MensajeTecnico = CONCAT_WS(' - ', 'ERROR AL REGISTRAR FUNCIONALIDAD', ERROR_PROCEDURE(), ERROR_LINE(), ERROR_MESSAGE());

            END CATCH
        END
    END

    -- UPDATE Feature --
    ELSE IF @w_Accion = 'U'
    BEGIN

        SELECT @w_featureStartDate = COALESCE(@i_featureStartDate,featureStartDate),
               @w_featureDueDate = COALESCE(@i_featureDueDate,featureDueDate)
        FROM [SQM_GENERAL].[TBL_Features] (NOLOCK)
        WHERE featureId = @i_featureId;

        IF ISNULL(@i_featureId,0) = 0
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL ID DE LA FUNCIONALIDAD ES OBLIGATORIO';
        END;

        ELSE IF ISNULL(@i_featureModificatorId,0) = 0
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL ID DEL MODIFICADOR ES OBLIGATORIO';
        END;

        ELSE IF NOT EXISTS (SELECT 1 FROM [SQM_GENERAL].[TBL_Features] (NOLOCK) WHERE featureId = @i_featureId)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'LA FUNCIONALIDAD NO EXISTE';
        END;

        ELSE IF NOT EXISTS (SELECT 1 FROM [SQM_SECURITY].[TBL_Users] (NOLOCK) WHERE userId = @i_featureModificatorId AND userEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'EL USUARIO MODIFICADOR NO EXISTE O NO ESTA HABILITADO';
        END;

        ELSE IF @i_featureSummary IS NOT NULL AND @i_featureSummary = ''
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'EL RESUMEN NO PUEDE ESTAR VACIO';
        END;

        ELSE IF @i_featureDescription IS NOT NULL AND @i_featureDescription = ''
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'LA DESCRIPCION NO PUEDE ESTAR VACIA';
        END;

        ELSE IF @i_featuresAcceptanceCriteria IS NOT NULL AND @i_featuresAcceptanceCriteria = ''
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'LOS CRITERIOS DE ACEPTACION NO PUEDEN ESTAR VACIOS';
        END;

        ELSE IF @i_featureParentLink IS NOT NULL AND NOT EXISTS (SELECT 1 FROM [SQM_GENERAL].[TBL_Epics] (NOLOCK) WHERE epicId = @i_featureParentLink)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'LA EPICA PADRE NO EXISTE';
        END;

        ELSE IF @i_featureOwner IS NOT NULL AND NOT EXISTS (SELECT 1 FROM [SQM_SECURITY].[TBL_Users] (NOLOCK) WHERE userId = @i_featureOwner AND userEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'EL PROPIETARIO NO EXISTE O NO ESTA HABILITADO';
        END;

        ELSE IF @i_featurePriority IS NOT NULL AND NOT EXISTS (SELECT 1 FROM [SQM_CATALOGS].[TBL_Priorities] (NOLOCK) WHERE priorityId = @i_featurePriority AND priorityEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'LA PRIORIDAD NO EXISTE O NO ESTA HABILITADA';
        END;

        ELSE IF @i_featureStatus IS NOT NULL AND NOT EXISTS (SELECT 1 FROM [SQM_CATALOGS].[TBL_Status] (NOLOCK) WHERE statusId = @i_featureStatus AND statusEnable = 1)
        BEGIN
            SET @o_Numero = 404;
            SET @o_MensajeUsuario = 'EL ESTADO NO EXISTE O NO ESTA HABILITADO';
        END;

        ELSE IF @w_featureStartDate IS NOT NULL AND @w_featureDueDate IS NOT NULL AND @w_featureDueDate < @w_featureStartDate
        BEGIN
            SET @o_Numero = 400;
            SET @o_MensajeUsuario = 'LA FECHA LIMITE NO PUEDE SER MENOR A LA FECHA INICIAL';
        END;

        ELSE
        BEGIN
            BEGIN TRANSACTION TRX_UPD_FEATURE;

            BEGIN TRY

                UPDATE [SQM_GENERAL].[TBL_Features]
                SET featureSummary = COALESCE(@i_featureSummary,featureSummary),
                    featureDescription = COALESCE(@i_featureDescription,featureDescription),
                    featuresAcceptanceCriteria = COALESCE(@i_featuresAcceptanceCriteria,featuresAcceptanceCriteria),
                    featureParentLink = COALESCE(@i_featureParentLink,featureParentLink),
                    featureOwner = COALESCE(@i_featureOwner,featureOwner),
                    featureStartDate = COALESCE(@i_featureStartDate,featureStartDate),
                    featureDueDate = COALESCE(@i_featureDueDate,featureDueDate),
                    featurePriority = COALESCE(@i_featurePriority,featurePriority),
                    featureStatus = COALESCE(@i_featureStatus,featureStatus),
                    featureModificationDate = @i_featureModificationDate,
                    featureModificatorId = @i_featureModificatorId
                WHERE featureId = @i_featureId;

                COMMIT TRANSACTION TRX_UPD_FEATURE;

                SET @o_Numero = 200;
                SET @o_MensajeUsuario = 'FUNCIONALIDAD ACTUALIZADA CORRECTAMENTE';

            END TRY

            BEGIN CATCH

                IF @@TRANCOUNT > 0
                    ROLLBACK TRANSACTION TRX_UPD_FEATURE;

                SET @o_Numero = 500;
                SET @o_MensajeUsuario = 'ERROR AL ACTUALIZAR FUNCIONALIDAD';
                SET @o_MensajeTecnico = CONCAT_WS(' - ', 'ERROR AL ACTUALIZAR FUNCIONALIDAD', ERROR_PROCEDURE(), ERROR_LINE(), ERROR_MESSAGE());

            END CATCH
        END
    END

    -- SELECT Feature --
    ELSE IF @w_Accion = 'S'
    BEGIN

        BEGIN TRY

            IF ISNULL(@i_PageNumber,0) < 1
                SET @i_PageNumber = 1;

            IF ISNULL(@i_RowsPerPage,0) < 1
                SET @i_RowsPerPage = 10;

            SELECT
                featureId,
                featureSummary,
                featureDescription,
                featuresAcceptanceCriteria,
                featureParentLink,
                featureOwner,
                featureStartDate,
                featureDueDate,
                featurePriority,
                featureCreationDate,
                featureCreatorId,
                featureModificationDate,
                featureModificatorId,
                featureStatus
            FROM [SQM_GENERAL].[TBL_Features] (NOLOCK)
            WHERE (@i_featureId IS NULL OR featureId = @i_featureId)
              AND (@i_featureParentLink IS NULL OR featureParentLink = @i_featureParentLink)
              AND (@i_featureOwner IS NULL OR featureOwner = @i_featureOwner)
              AND (@i_featureStatus IS NULL OR featureStatus = @i_featureStatus)
            ORDER BY featureId
            OFFSET (@i_PageNumber - 1) * @i_RowsPerPage ROWS
            FETCH NEXT @i_RowsPerPage ROWS ONLY;

            SET @w_totalRows = @@ROWCOUNT;

            IF (@w_totalRows > 0)
            BEGIN
                SET @o_Numero = 200;
                SET @o_MensajeUsuario = 'FUNCIONALIDADES LISTADAS CORRECTAMENTE';
            END
            ELSE
            BEGIN
                SET @o_Numero = 204;
                SET @o_MensajeUsuario = 'NO HAY MAS REGISTROS PARA LISTAR';
            END
        END TRY

        BEGIN CATCH

            SET @o_Numero = 500;
            SET @o_MensajeUsuario = 'ERROR AL LISTAR FUNCIONALIDADES';
            SET @o_MensajeTecnico = CONCAT_WS(' - ', 'ERROR AL LISTAR FUNCIONALIDADES', ERROR_PROCEDURE(), ERROR_LINE(), ERROR_MESSAGE());

        END CATCH

    END

    -- ACCION INVALIDA --
    ELSE
    BEGIN

        SET @o_Numero = 405;
        SET @o_MensajeUsuario = 'METODO NO HABILITADO';
        SET @o_MensajeTecnico = 'EL PROCEDIMIENTO ALMACENADO NO TIENE HABILITADA ESA OPCION';

    END

END;
GO