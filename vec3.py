from __future__ import annotations

from dataclasses import dataclass, field
import math
import random

@dataclass(frozen=True, slots=True)
class Vec3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __neg__(self) -> Vec3:
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, other: Vec3) -> Vec3:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vec3) -> Vec3:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, t: float) -> Vec3:
        return Vec3(self.x * t, self.y * t, self.z * t)

    def __rmul__(self, t: float) -> Vec3:
        return self * t

    def __truediv__(self, t: float) -> Vec3:
        return self * (1.0 / t)

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def length_squared(self) -> float:
        return Vec3.dot(self, self)

    def unit_vector(self) -> Vec3:
        return self / self.length()

    @staticmethod
    def random(min: float = 0.0, max: float = 1.0) -> Vec3:
        return Vec3(random.uniform(min, max), random.uniform(min, max), random.uniform(min, max))

    @staticmethod
    def random_in_unit_sphere() -> Vec3:
        while True:
            p = Vec3.random(-1.0, 1.0)
            if p.length_squared() < 1.0:
                return p

    @staticmethod
    def random_unit_vector() -> Vec3:
        return Vec3.random_in_unit_sphere().unit_vector()

    @staticmethod
    def random_on_hemisphere(normal: Vec3) -> Vec3:
        on_unit_sphere = Vec3.random_unit_vector()
        if Vec3.dot(on_unit_sphere, normal) > 0.0:
            return on_unit_sphere
        else:
            return -on_unit_sphere

    @staticmethod
    def dot(u: Vec3, v: Vec3) -> float:
        return (u.x * v.x) + (u.y * v.y) + (u.z * v.z)

    @staticmethod
    def cross(u: Vec3, v: Vec3) -> float:
        return Vec3(((u.y * v.z) - (u.z * v.y)),
                    ((u.z * v.x) - (u.x * v.z)),
                    ((u.x * v.y) - (u.y * v.x)))

Color=Vec3
Point3=Vec3
