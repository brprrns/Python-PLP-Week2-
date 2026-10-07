from dataclasses import dataclass


@dataclass
class Student:
    name: str
    scores: list[float]

    @property
    def average(self) -> float:
        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)