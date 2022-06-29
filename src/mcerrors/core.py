from typing import List
from typing import Callable
import random


class DistVariable:

    def __init__(self, distribution: List[float]) -> None:
        self._arr = distribution

    def sample(self) -> float:
        return random.choice(self._arr)


class Propagator:

    def __init__(self, prop_func: Callable[..., float]) -> None:
        self.func = prop_func

    def addDistVariable(self, variable: DistVariable) -> None:
        self.input_vars.append(variable)

    def propagate(self, samples: int) -> List[float]:
        
