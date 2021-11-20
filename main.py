import pygame as pg
import random
import math
import ctypes

user32 = ctypes.windll.user32


res = WIDTH, HEIGTH = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
FPS = 60
COL_STAR = 2000

vec2, vec3 = pg.math.Vector2, pg.math.Vector3
CENTER = vec2(WIDTH // 2, HEIGTH // 2)
COLORS = 'white grey blue cyan skyblue purple magenta'.split()
# Z_DISTANCE = 40
Z_DISTANCE = 190
# ALPHA = 120
ALPHA = 90


class Star:
    def __init__(self, app):
        self.screen = app.screen
        self.pos3d = self.get_pos3d()
        self.vel = random.uniform(0.25, 0.75)
        self.color = random.choice(COLORS)
        self.screen_pos = vec2(0, 0)
        self.size = 10

    def get_pos3d(self, scale_pos=50):
        angel = random.uniform(0, 2 * math.pi)
        radius = random.randrange(HEIGTH // 5, HEIGTH) * scale_pos
        x = radius * math.sin(angel)
        y = radius * math.cos(angel)
        return vec3(x, y, Z_DISTANCE)

    def update(self):
        self.pos3d.z -= self.vel
        self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d

        self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER
        self.size = (Z_DISTANCE - self.pos3d.z) / (0.5 * self.pos3d.z)

        self.pos3d.xy = self.pos3d.xy.rotate(0.02)

    def draw(self):
        pg.draw.circle(self.screen, self.color, self.screen_pos, self.size)


class Starfield:
    def __init__(self, app):
        self.stars = [Star(app) for _ in range(COL_STAR)]

    def run(self):
        [star.update() for star in self.stars]
        self.stars.sort(key=lambda star: star.pos3d.z, reverse=True)
        [star.draw() for star in self.stars]

class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res)
        self.alpha_surface = pg.Surface(res)
        self.alpha_surface.set_alpha(ALPHA)
        self.clock = pg.time.Clock()
        self.starfield = Starfield(self)

    def run(self):
        pg.mouse.set_visible(False)
        while True:
            # self.screen.fill('black')
            self.screen.blit(self.alpha_surface, (0, 0))
            self.starfield.run()

            pg.display.flip()
            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()