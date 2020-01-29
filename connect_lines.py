import pygame as pg
import random as rnd
import math


class Graph:

    def __init__(self, vert_num):
        self.vertice = [[rnd.randint(0, display_size[0]), rnd.randint(0, display_size[1])] for _ in range(vert_num)]
        self.edge = list()
        self.last_move = [[0, 0] for _ in self.vertice]

    def move_vertices(self, scene_size):
        for id in range(len(self.vertice)):

            move = [rnd.randint(-1, 1) + self.last_move[id][0], rnd.randint(-1, 1) + self.last_move[id][1]]
            if move[0] > 10:
                move[0] = 10
            if move[1] > 10:
                move[1] = 10

            self.vertice[id][0] = (self.vertice[id][0] + move[0]) % scene_size[0]
            self.vertice[id][1] = (self.vertice[id][1] + move[1]) % scene_size[1]

            self.last_move[id] = move

    def find_close_points(self, dist):

        x_struct = sorted(self.vertice, key=lambda x: x[0])

        self.edge.clear()
        for v in x_struct:
            for u in x_struct:
                if v != u and \
                        math.sqrt(pow(u[0] - v[0], 2) + pow(u[1] - v[1], 2)) < dist:
                    self.edge.append([v, u])

    def draw(self, win):
        win.fill((66, 66, 66))
        for point in graph.vertice:
            pg.draw.circle(win, (200, 200, 200), point, 2)
        for line in self.edge:
            pg.draw.line(win, (200, 200, 200), line[0], line[1], 1)


if __name__ == '__main__':

    display_size = [1200, 900]
    window = pg.display.set_mode(display_size)

    clock = pg.time.Clock()
    run_flag = True
    graph = Graph(200)

    while run_flag:

        clock.tick(30)

        for eve in pg.event.get():
            if eve.type == pg.QUIT:
                run_flag = False

        graph.find_close_points(40)

        graph.draw(window)
        pg.display.update()
        graph.move_vertices(display_size)
