from array import array
from collections.abc import Iterator
from typing import Literal, overload

import numpy as np
from numpy.typing import DTypeLike, NDArray

class CoordinateSequence:
    def __init__(self, coords: NDArray[np.float64]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[float, ...]]: ...
    @overload
    def __getitem__(self, key: int) -> tuple[float, ...]: ...
    @overload
    def __getitem__(self, key: slice) -> list[tuple[float, ...]]: ...
    def __array__(self, dtype: DTypeLike | None = None, copy: Literal[True] | None = None) -> NDArray[np.float64]: ...
    @property
    def xy(self) -> tuple[array[float], array[float]]: ...
