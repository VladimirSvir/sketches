import pygame as pg
import random
import math


res = WIDTH, HEIGTH = 1600, 900
FPS = 120
COL_STAR = 100

vec2, vec3 = pg.math.Vector2, pg.math.Vector3
CENTER = vec2(WIDTH // 2, HEIGTH // 2)
COLORS = 'red green blue orange purple cyan white'.split()
Z_DISTANCE = 30


class Star:
    def __init__(self, app):
        self.screen = app.screen
        self.pos3d = self.get_pos3d()
        self.vel = random.uniform(0.005, 0.175)
        self.color = random.choice(COLORS)
        self.screen_pos = vec2(0, 0)
        self.size = 5

    def get_pos3d(self):
        angel = random.uniform(0, 2 * math.pi)
        radius = random.randrange(HEIGTH)
        x = radius * math.sin(angel)
        y = radius * math.cos(angel)
        return vec3(x, y, Z_DISTANCE)

    def update(self):
        self.pos3d.z -= self.vel
        self.pos3d = self.get_pos3d() if self.pos3d.z < 1 else self.pos3d

        self.screen_pos = vec2(self.pos3d.x, self.pos3d.y) / self.pos3d.z + CENTER
        self.size = Z_DISTANCE / self.pos3d.z

    def draw(self):
        pg.draw.circle(self.screen, self.color, self.screen_pos, self.size)


class Starfield:
    def __init__(self, app):
        self.stars = [Star(app) for _ in range(COL_STAR)]

    def run(self):
        [star.update() for star in self.stars]
        [star.draw() for star in self.stars]

class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.starfield = Starfield(self)

    def run(self):
        while True:
            self.screen.fill('black')
            self.starfield.run()

            pg.display.flip()
            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()