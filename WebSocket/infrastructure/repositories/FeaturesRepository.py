from domain.entities.FeaturesModels import FeaturesCreate, FeaturesUpdate
from domain.interfaces.IFeaturesRepository import IFeaturesRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class FeaturesRepository(StoredProcedureRepository, IFeaturesRepository):
    SP_NAME = "[SQM_GENERAL].[USP_Features]"

    def insert_feature(self, feature: FeaturesCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_featureSummary": feature.featureSummary,
            "i_featureDescription": feature.featureDescription,
            "i_featuresAcceptanceCriteria": feature.featuresAcceptanceCriteria,
            "i_featureParentLink": feature.featureParentLink,
            "i_featureOwner": feature.featureOwner,
            "i_featureStartDate": feature.featureStartDate,
            "i_featureDueDate": feature.featureDueDate,
            "i_featurePriority": feature.featurePriority,
            "i_featureCreatorId": creator_id,
            "i_featureStatus": feature.featureStatus,
        })

    def update_feature(self, feature: FeaturesUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_featureId": feature.featureId,
            "i_featureSummary": feature.featureSummary,
            "i_featureDescription": feature.featureDescription,
            "i_featuresAcceptanceCriteria": feature.featuresAcceptanceCriteria,
            "i_featureParentLink": feature.featureParentLink,
            "i_featureOwner": feature.featureOwner,
            "i_featureStartDate": feature.featureStartDate,
            "i_featureDueDate": feature.featureDueDate,
            "i_featurePriority": feature.featurePriority,
            "i_featureModificatorId": modificator_id,
            "i_featureStatus": feature.featureStatus,
        })

    def list_features(self, page_number: int, rows_per_page: int, feature_id: int | None = None,
                      feature_parent_link: int | None = None, feature_owner: int | None = None,
                      feature_status: int | None = None):
        return self.execute_procedure("S", {
            "i_featureId": feature_id,
            "i_featureParentLink": feature_parent_link,
            "i_featureOwner": feature_owner,
            "i_featureStatus": feature_status,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
