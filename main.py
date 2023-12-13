#!/usr/bin/env python3

from camera import *
from hittable_list import *
from material import *
from sphere import *
from vec3 import *

def main() -> None:
    world = HittableList()

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Lambertian(Color(0.7, 0.3, 0.3))
    material_left   = Metal(Color(0.8, 0.8, 0.8), 0.3)
    material_right  = Metal(Color(0.8, 0.6, 0.2), 1.0)

    world.add(Sphere(Point3( 0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(Point3( 0.0,    0.0, -1.0),   0.5, material_center))
    world.add(Sphere(Point3(-1.0,    0.0, -1.0),   0.5, material_left))
    world.add(Sphere(Point3( 1.0,    0.0, -1.0),   0.5, material_right))

    cam = Camera()
    cam.aspect_ratio = 16.0 / 9.0
    cam.image_width = 400
    cam.samples_per_pixel = 100
    cam.max_depth = 50
    cam.show_preview = True

    cam.render(world)

if __name__ == '__main__':
    main()
