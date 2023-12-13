from __future__ import annotations

from hittable import *
from interval import *

class HittableList(Hittable):
    def __init__(self) -> None:
        self._objects = list()

    def add(self, o: Hittable) -> None:
        self._objects.append(o)

    def clear(self) -> None:
        self._objects = list()

    def hit(self, r: Ray, ray_t: Interval) -> HitRecord:
        rec = None
        closest_so_far = ray_t.max
        for o in self._objects:
            temp_rec = o.hit(r, Interval(ray_t.min, closest_so_far))
            if temp_rec:
                closest_so_far = temp_rec.t
                rec = temp_rec

        return rec
