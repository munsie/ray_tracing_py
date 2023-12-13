#!/usr/bin/env python3

import ansi
import sys

from camera import *
from hittable_list import *
from sphere import *
from vec3 import *

def main() -> None:
    world = HittableList()
    world.add(Sphere(Point3(0.0,    0.0, -1.0),   0.5))
    world.add(Sphere(Point3(0.0, -100.5, -1.0), 100.0))

    cam = Camera()
    cam.aspect_ratio = 16.0 / 9.0
    cam.image_width = 400
    cam.samples_per_pixel = 100
    cam.max_depth = 50
    cam.show_preview = True

    cam.render(world)

if __name__ == '__main__':
    main()
