# Stubs for pyspark.ml.tuning (Python 3.5)
#

from typing import overload
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar

from pyspark.ml._typing import ParamMap
from pyspark.ml import Estimator, Model
from pyspark.ml.evaluation import Evaluator
from pyspark.ml.param import Param
from pyspark.ml.param.shared import *
from pyspark.ml.util import *

P = TypeVar("P")

class ParamGridBuilder:
    def __init__(self) -> None: ...
    def addGrid(self, param: Param, values: List[Any]) -> 'ParamGridBuilder': ...
    @overload
    def baseOn(self, __args: ParamMap) -> ParamGridBuilder: ...
    @overload
    def baseOn(self, *args: Tuple[Param, Any]) -> ParamGridBuilder: ...
    def build(self) -> List[ParamMap]: ...

class ValidatorParams(HasSeed):
    estimator = ...  # type: Param
    estimatorParamMaps = ...  # type: Param
    evaluator = ...  # type: Param
    def setEstimator(self: P, value: Estimator) -> P: ...
    def getEstimator(self) -> Estimator: ...
    def setEstimatorParamMaps(self: P, value: List[ParamMap]) -> P: ...
    def getEstimatorParamMaps(self) -> List[ParamMap]: ...
    def setEvaluator(self: P, value: Evaluator) -> P: ...
    def getEvaluator(self) -> Evaluator: ...

class CrossValidator(Estimator[CrossValidatorModel], ValidatorParams, HasParallelism, HasCollectSubModels, MLReadable[CrossValidator], MLWritable):
    numFolds = ...  # type: Param
    def __init__(self, estimator: Optional[Estimator] = ..., estimatorParamMaps: Optional[List[ParamMap]] = ..., evaluator: Optional[Evaluator] = ..., numFolds: int = ..., seed: Optional[int] = ..., parallelism: int = ..., collectSubModels: bool = ...) -> None: ...
    def setParams(self, estimator: Optional[Estimator] = ..., estimatorParamMaps: Optional[List[ParamMap]] = ..., evaluator: Optional[Evaluator] = ..., numFolds: int = ..., seed: Optional[int] = ..., parallelism: int = ..., collectSubModels: bool = ...) -> CrossValidator: ...
    def setNumFolds(self, value: int) -> CrossValidator: ...
    def getNumFolds(self) -> int: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> CrossValidator: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[CrossValidator]) -> MLReader: ...

class CrossValidatorModel(Model, ValidatorParams, MLReadable[CrossValidatorModel], MLWritable):
    bestModel = ...  # type: Model
    avgMetrics = ...  # type: List[float]
    subModels = ...  # type: List[List[Model]]
    def __init__(self, bestModel: Model, avgMetrics: List[float] = ...,  subModels: Optional[List[List[Model]]] = ...) -> None: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> CrossValidatorModel: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[CrossValidatorModel]) -> MLReader: ...

class TrainValidationSplit(Estimator[TrainValidationSplitModel], ValidatorParams, HasParallelism, HasCollectSubModels, MLReadable[TrainValidationSplit], MLWritable):
    trainRatio = ...  # type: Param
    def __init__(self, estimator: Optional[Estimator] = ..., estimatorParamMaps: Optional[List[ParamMap]] = ..., evaluator: Optional[Evaluator] = ..., trainRatio: float = ..., parallelism: int = ..., collectSubModels: bool = ..., seed: Optional[int] = ...) -> None: ...
    def setParams(self, estimator: Optional[Estimator] = ..., estimatorParamMaps: Optional[List[ParamMap]] = ..., evaluator: Optional[Evaluator] = ..., trainRatio: float = ..., parallelism: int = ..., collectSubModels: bool = ..., seed: Optional[int] = ...) -> TrainValidationSplit: ...
    def setTrainRatio(self, value: float) -> TrainValidationSplit: ...
    def getTrainRatio(self) -> float: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> TrainValidationSplit: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[TrainValidationSplit]) -> MLReader: ...

class TrainValidationSplitModel(Model, ValidatorParams, MLReadable[TrainValidationSplitModel], MLWritable):
    bestModel = ...  # type: Model
    validationMetrics = ...  # type: List[float]
    subModels = ...  # type: List[Model]
    def __init__(self, bestModel: Model, validationMetrics: List[float] = ..., subModels: Optional[List[Model]] = ...) -> None: ...
    def copy(self, extra: Optional[ParamMap] = ...) -> TrainValidationSplitModel: ...
    def write(self) -> MLWriter: ...
    @classmethod
    def read(cls: Type[TrainValidationSplitModel]) -> MLReader: ...
