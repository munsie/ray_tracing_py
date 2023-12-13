from __future__ import annotations

from dataclasses import dataclass, field
from interval import *
from material import *
from ray import *
from vec3 import *

@dataclass(slots=True)
class HitRecord:
    p: Point3 = Point3()
    normal: Vec3 = Vec3()
    material: Material = Material()
    t: float = 0.0
    front_face: bool = False

    def set_face_normal(self, r: Ray, outward_normal: Vec3) -> None:
        self.front_face = Vec3.dot(r.direction, outward_normal) < 0.0
        self.normal = outward_normal if self.front_face else -outward_normal

class Hittable:
    def hit(self, r: Ray, ray_t: Interval) -> HitRecord:
        return None
