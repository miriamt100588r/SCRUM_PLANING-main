from abc import ABC, abstractmethod

from domain.entities.FeaturesModels import FeaturesCreate, FeaturesUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IFeaturesRepository(ABC):
    @abstractmethod
    def insert_feature(self, feature: FeaturesCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_feature(self, feature: FeaturesUpdate, modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_features(self, page_number: int, rows_per_page: int, feature_id: int | None = None,
                      feature_parent_link: int | None = None, feature_owner: int | None = None,
                      feature_status: int | None = None) -> QueryResult:
        raise NotImplementedError
