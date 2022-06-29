from typing import List
from typing import Callable


class DistVariable:

    _arr: List[float]

    def __init__(self, distribution: List[float]) -> None: ...

    def sample(self) -> float: ...


class Propagator:

    func: Callable[..., float]
    input_vars: List[DistVariable]
    samples: List[float]

    def __init__(self, prop_func: Callable[..., float]) -> None: ...

    def addDistVariable(self, variable: DistVariable) -> None: ...

    def propagate(self, samples: int) -> List[float]: ...
