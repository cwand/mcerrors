from typing import List
import random


class DistVariable:

    def __init__(self, distribution: List[float]):
        self.arr = distribution

    def sample(self) -> float:
        return random.choice(self.arr)
