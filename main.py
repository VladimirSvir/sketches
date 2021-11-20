import pygame as pg

res = WIDTH, HEIGTH = 1600, 900
FPS = 120

class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.screen.fill('black')

            pg.display.flip()
            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App()
    app.run()