from __future__ import annotations

from dataclasses import dataclass, field
import math
import random
import util

@dataclass(frozen=True, slots=True)
class Vec3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __neg__(self) -> Vec3:
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, other: float | int | Vec3) -> Vec3:
        if type(other) is Vec3:
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return Vec3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other: float | int | Vec3) -> Vec3:
        if type(other) is Vec3:
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return Vec3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other: float | int | Vec3) -> Vec3:
        if type(other) is Vec3:
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

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

    def clamp(self) -> Vec3:
        return Vec3(util.clamp(self.x), util.clamp(self.y), util.clamp(self.z))

    def linear_to_gamma(self) -> Vec3:
        return Vec3(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z))

    def near_zero(self) -> bool:
        s = 1e-8
        return (math.fabs(self.x) < s) and (math.fabs(self.y) < s) and (math.fabs(self.z) < s)
    
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

    @staticmethod
    def reflect(v: Vec3, n: Vec3) -> Vec3:
        return v - 2.0 * Vec3.dot(v, n) * n

    @staticmethod
    def refract(uv: Vec3, n: Vec3, etai_over_etat: float) -> Vec3:
        cos_theta = min(Vec3.dot(-uv, n), 1.0)
        r_out_perp = etai_over_etat * (uv + cos_theta * n)
        r_out_parallel = -math.sqrt(math.fabs(1.0 - r_out_perp.length_squared())) * n
        return r_out_perp + r_out_parallel

Color=Vec3
Point3=Vec3
