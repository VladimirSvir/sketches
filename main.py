import pygame as pg

res = WIDTH, HEIGTH = 1600, 900
FPS = 120
COL_STAR = 1000

class Star:
    def __init__(self, app):
        pass

    def update(self):
        pass

    def draw(self):
        pass


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