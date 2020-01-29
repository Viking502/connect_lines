import pygame as pg
import random as rnd

if __name__ == '__main__':

    display_size = [1200, 900]
    window = pg.display.set_mode(display_size)

    clock = pg.time.Clock()
    run_flag = True

    point_num = 20
    point = [{'x': rnd.randint(0, display_size[0]), 'y': rnd.randint(0, display_size[1])} for _ in range(point_num)]

    while run_flag:

        clock.tick(30)

        for p in point:
            pg.draw.circle(window, (0, 255, 0), 2, 0)
        pg.display.update()