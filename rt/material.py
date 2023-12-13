from __future__ import annotations

from hittable import *
from ray import *
from vec3 import *

class Material:
    def scatter(self, r_in: Ray, rec: HitRecord, attenuation: Color) -> tuple[Ray, Color]:
        return None, None

class Lambertian(Material):
    def __init__(self, albedo: Color) -> None:
        self._albedo = albedo

    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color]:
        scatter_direction = rec.normal + Vec3.random_unit_vector()
        
        # catch degenerate scatter direction
        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        return Ray(rec.p, scatter_direction), self._albedo

class Metal(Material):
    def __init__(self, albedo: Color, fuzz: float) -> None:
        self._albedo = albedo
        self._fuzz = min(fuzz, 1.0)

    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color]:
        reflected = Vec3.reflect(Vec3.unit_vector(r_in.direction), rec.normal)
        scattered = Ray(rec.p, reflected + self._fuzz * Vec3.random_unit_vector())
        if Vec3.dot(scattered.direction, rec.normal) > 0.0:
            return scattered, self._albedo
        else:
            return None, None

class Dielectric(Material):
    def __init__(self, index_of_refraction: float, albedo: Color = Color(1.0, 1.0, 1.0)) -> None:
        self._index_of_refraction = index_of_refraction
        self._albedo = albedo
    
    def scatter(self, r_in: Ray, rec: HitRecord) -> tuple[Ray, Color]:
        refraction_ratio = (1.0 / self._index_of_refraction) if rec.front_face else self._index_of_refraction

        unit_direction = Vec3.unit_vector(r_in.direction)
        
        cos_theta = min(Vec3.dot(-unit_direction, rec.normal), 1.0)
        sin_theta = math.sqrt(1.0 - cos_theta * cos_theta);

        cannot_refract = (refraction_ratio * sin_theta) > 1.0
        if cannot_refract or Dielectric._reflectance(cos_theta, refraction_ratio) > random.random():
            direction = Vec3.reflect(unit_direction, rec.normal)
        else:
            direction = Vec3.refract(unit_direction, rec.normal, refraction_ratio)

        return Ray(rec.p, direction), self._albedo

    @staticmethod
    def _reflectance(cosine: float, ref_idx: float) -> float:
        # Use Schlick's approximation for reflectance.
        r0 = (1.0 - ref_idx) / (1.0 + ref_idx)
        r0 *= r0
        return r0 + (1.0 - r0) * math.pow((1.0 - cosine), 5.0)

