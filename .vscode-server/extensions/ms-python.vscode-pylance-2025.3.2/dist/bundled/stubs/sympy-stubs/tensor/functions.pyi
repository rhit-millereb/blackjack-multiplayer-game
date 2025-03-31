from functools import singledispatch
from typing_extensions import Self

from sympy import Mul
from sympy.core.expr import Expr

class TensorProduct(Expr):
    is_number = ...
    def __new__(cls, *args, **kwargs) -> Self: ...
    def rank(self) -> int: ...
    @property
    def shape(self) -> tuple[()]: ...
    def __getitem__(self, index) -> Mul: ...

@singledispatch
def shape(expr): ...

class NoShapeError(Exception): ...
