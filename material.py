from __future__ import annotations

from hittable import *
from ray import *
from vec3 import *

class Material:
    def scatter(self, r_in: Ray, rec: HitRecord, attenuation: Color) -> tuple[Ray, Color]:
        return None, None

class Lambertian:
    def __init__(self, albedo: Color) -> None:
        self._albedo = albedo

    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color]:
        scatter_direction = rec.normal + Vec3.random_unit_vector()
        
        # catch degenerate scatter direction
        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        return Ray(rec.p, scatter_direction), self._albedo

class Metal:
    def __init__(self, albedo: Color) -> None:
        self._albedo = albedo

    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color]:
        reflected = Vec3.reflect(Vec3.unit_vector(r_in.direction), rec.normal)
        return Ray(rec.p, reflected), self._albedo

