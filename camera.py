from __future__ import annotations

from hittable import *
from ppm import *
from ray import *
from vec3 import *

import datetime
import pygame
import random
import time

class Camera:
    aspect_ratio: float = 1.0       # ratio of image width over height
    image_width: int = 100          # rendered image width in pixel count
    samples_per_pixel: int = 10     # count of random samples for each pixel
    max_depth: int = 10             # maximum number of ray bounces into scene
    show_preview: bool = False      # show a preview window while rendering

    def __init__(self):
        pass

    def render(self, world: Hittable) -> None:
        start_time = time.time()

        self._initialize()

        if self.show_preview:
            pygame.init()
            screen = pygame.display.set_mode((self.image_width, self._image_height))
            pygame.display.set_caption("Ray Tracer")
            screen.fill((128, 128, 128))
            pygame.display.flip()

        ppm_file = ppm('image.ppm', self.image_width, self._image_height, progress=True)
        
        for j in range(self._image_height):
            for i in range(self.image_width):
                pixel_color = Color()
                for _ in range(self.samples_per_pixel):
                    r = self._get_ray(i, j)
                    pixel_color += self._ray_color(r, self.max_depth, world)
                
                pixel_color /= self.samples_per_pixel

                ppm_file.write(pixel_color)

                if self.show_preview:
                    screen.set_at((i, j), (pixel_color.x * 255.0, pixel_color.y * 255.0, pixel_color.z * 255.0))
                
            if self.show_preview:
                pygame.display.update(pygame.Rect(0, j, self.image_width, 1))
                
                # service the event queue
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
    
        render_time = time.time() - start_time
        print(f'Render finished in {datetime.timedelta(seconds = render_time)}.')

        # wait for the user to close the window if we are showing a preview
        while self.show_preview:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

    def _initialize(self) -> None:
        self._image_height = int(self.image_width / self.aspect_ratio)
        self._image_height = 1 if self._image_height < 1 else self._image_height

        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * (self.image_width / self._image_height)
        self._center = Point3()

        # calculate the vectors across the horizontal and down the vertical viewport edges
        viewport_u = Vec3(viewport_width, 0.0, 0.0)
        viewport_v = Vec3(0.0, -viewport_height, 0.0)

        # calculate the horizontal and vertical delta vectors from pixel to pixel
        self._pixel_delta_u = viewport_u / self.image_width
        self._pixel_delta_v = viewport_v / self._image_height

        # calculate the location of the upper left pixel
        self._viewport_upper_left = self._center - Vec3(0.0, 0.0, focal_length) - (viewport_u / 2.0) - (viewport_v / 2.0)
        self._pixel00_loc = self._viewport_upper_left + 0.5 * (self._pixel_delta_u + self._pixel_delta_v)

    def _get_ray(self, i: int, j: int) -> Ray:
        # get a randomly sampled camera ray for the pixel at location i, j
        pixel_center = self._pixel00_loc + (i * self._pixel_delta_u) + (j * self._pixel_delta_v)
        pixel_sample = pixel_center + self._pixel_sample_square()

        ray_direction = pixel_sample - self._center
        return Ray(self._center, ray_direction)
    
    def _pixel_sample_square(self) -> Vec3:
        return (random.uniform(-0.5, 0.5) * self._pixel_delta_u) + (random.uniform(-0.5, 0.5) * self._pixel_delta_v)
    
    def _ray_color(self, r: Ray, depth: int, world: Hittable) -> Color:
        # if we've exceeded the ray bounce limit, no more light is gathered
        if depth <= 0:
            return Color()

        rec = world.hit(r, Interval(0.001, float('inf')))
        if rec:
            direction = rec.normal + Vec3.random_unit_vector()
            return 0.5 * self._ray_color(Ray(rec.p, direction), depth - 1, world)

        unit_direction = r.direction.unit_vector()
        a = 0.5 * (unit_direction.y + 1.0)
        return (1.0 - a) * Color(1.0, 1.0, 1.0) + a * Color(0.5, 0.7, 1.0)
