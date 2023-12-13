from __future__ import annotations

from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Interval:
    min: float = float('-inf')
    max: float = float('inf')

    def contains(self, x: float) -> bool:
        return self.min <= x and x <= self.max

    def surrounds(self, x: float) -> bool:
        return self.min < x and x < self.max

Empty = Interval(float('inf'), float('-inf'))
Universe = Interval()
