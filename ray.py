from __future__ import annotations

from dataclasses import dataclass, field
from vec3 import *

@dataclass(frozen=True, slots=True)
class Ray:
    origin: Point3 = Point3()
    direction: Vec3 = Vec3()

    def at(self, t: float) -> Point3:
        return self.origin + (self.direction * t)
