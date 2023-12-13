from __future__ import annotations

from dataclasses import dataclass, field
from hittable import *
from interval import *
from vec3 import *

import math

class Sphere(Hittable):
    def __init__(self, center: Point3, radius: float):
        self._center = center
        self._radius = radius

    def hit(self, r: Ray, ray_t: Interval) -> HitRecord:
        oc = r.origin - self._center
        a = r.direction.length_squared()
        half_b = Vec3.dot(oc, r.direction)
        c = oc.length_squared() - self._radius * self._radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return None
        sqrtd = math.sqrt(discriminant)

        # find the nearest root that lies in the acceptable range
        root = (-half_b - sqrtd) / a
        if not ray_t.surrounds(root):
            root = (-half_b + sqrtd) / a
            if not ray_t.surrounds(root):
                return None

        rec = HitRecord()
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self._center) / self._radius
        rec.set_face_normal(r, outward_normal)

        return rec
