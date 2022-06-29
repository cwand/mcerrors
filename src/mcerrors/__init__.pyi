from typing import List

class DistVariable:

    def __init__(self, distribution: List[float]) -> None: ...

    def sample(self) -> float: ...
