from domain.entities.FeaturesModels import FeaturesCreate, FeaturesUpdate
from domain.interfaces.IFeaturesRepository import IFeaturesRepository


class FeatureUseCase:
    def __init__(self, repository: IFeaturesRepository):
        self.repository = repository

    def create_feature(self, feature: FeaturesCreate, creator_id: int):
        return self.repository.insert_feature(feature, creator_id)

    def update_feature(self, feature: FeaturesUpdate, modificator_id: int):
        return self.repository.update_feature(feature, modificator_id)

    def list_features(self, page_number: int, rows_per_page: int, feature_id: int | None = None,
                      feature_parent_link: int | None = None, feature_owner: int | None = None,
                      feature_status: int | None = None):
        return self.repository.list_features(
            page_number, rows_per_page, feature_id, feature_parent_link, feature_owner, feature_status
        )
