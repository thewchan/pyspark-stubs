# Stubs for pyspark.ml.image (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class _ImageSchema:
    def __init__(self) -> None: ...
    @property
    def imageSchema(self): ...
    @property
    def ocvTypes(self): ...
    @property
    def columnSchema(self): ...
    @property
    def imageFields(self): ...
    @property
    def undefinedImageType(self): ...
    def toNDArray(self, image: Any): ...
    def toImage(self, array: Any, origin: str = ...): ...

ImageSchema: Any
