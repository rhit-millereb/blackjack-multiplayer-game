from typing import Any, Literal

from sympy.polys.agca.modules import FreeModulePolyRing
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.compositedomain import CompositeDomain
from sympy.polys.domains.ring import Ring
from sympy.polys.polyclasses import DMF, DMP
from sympy.series.order import Order
from sympy.utilities import public

class PolynomialRingBase(Ring, CharacteristicZero, CompositeDomain):
    has_assoc_Ring = ...
    has_assoc_Field = ...
    default_order = ...
    def __init__(self, dom, *gens, **opts) -> None: ...
    def new(self, element): ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def from_ZZ(K1, a, K0): ...
    def from_ZZ_python(K1, a, K0): ...
    def from_QQ(K1, a, K0): ...
    def from_QQ_python(K1, a, K0): ...
    def from_ZZ_gmpy(K1, a, K0): ...
    def from_QQ_gmpy(K1, a, K0): ...
    def from_RealField(K1, a, K0): ...
    def from_AlgebraicField(K1, a, K0) -> None: ...
    def from_PolynomialRing(K1, a, K0): ...
    def from_GlobalPolynomialRing(K1, a, K0): ...
    def get_field(self) -> Any: ...
    def poly_ring(self, *gens): ...
    def frac_field(self, *gens): ...
    def revert(self, a): ...
    def gcdex(self, a, b): ...
    def gcd(self, a, b): ...
    def lcm(self, a, b): ...
    def factorial(self, a): ...
    def free_module(self, rank) -> FreeModulePolyRing: ...

@public
class GlobalPolynomialRing(PolynomialRingBase):
    is_Poly = ...
    dtype = DMP
    def from_FractionField(K1, a, K0) -> None: ...
    def to_sympy(self, a) -> Order: ...
    def from_sympy(self, a): ...
    def is_positive(self, a): ...
    def is_negative(self, a): ...
    def is_nonpositive(self, a): ...
    def is_nonnegative(self, a): ...

class GeneralizedPolynomialRing(PolynomialRingBase):
    dtype = DMF
    def new(self, a) -> dtype: ...
    def __contains__(self, a) -> Literal[False]: ...
    def from_FractionField(K1, a, K0): ...
    def to_sympy(self, a): ...
    def from_sympy(self, a): ...

@public
def PolynomialRing(dom, *gens, **opts) -> Any | GeneralizedPolynomialRing: ...
