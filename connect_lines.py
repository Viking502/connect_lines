import pygame as pg
import random as rnd
import math


class Graph:

    def __init__(self, vert_num, max_distance=40, max_velocity=6):
        self.vertice = [[rnd.randint(0, display_size[0]), rnd.randint(0, display_size[1])] for _ in range(vert_num)]
        self.edge = list()
        self.last_move = [[0, 0] for _ in self.vertice]
        self.max_dist = max_distance
        self.max_vel = max_velocity

    def move_vertices(self, scene_size):
        for id in range(len(self.vertice)):

            move = [rnd.randint(-1, 1) + self.last_move[id][0], rnd.randint(-1, 1) + self.last_move[id][1]]
            if abs(move[0]) > self.max_vel:
                move[0] = self.max_vel
            if abs(move[1]) > self.max_vel:
                move[1] = self.max_vel

            self.vertice[id][0] = (self.vertice[id][0] + move[0]) % scene_size[0]
            self.vertice[id][1] = (self.vertice[id][1] + move[1]) % scene_size[1]

            self.last_move[id] = move

    def find_close_points(self):

        x_struct = sorted(self.vertice, key=lambda x: x[0])

        self.edge.clear()
        for v in x_struct:
            for u in x_struct:
                dist = math.sqrt(pow(u[0] - v[0], 2) + pow(u[1] - v[1], 2))
                if v != u and dist < self.max_dist:
                    self.edge.append([v, u, int(dist)])

    def draw(self, win):
        win.fill((66, 66, 66))
        for point in graph.vertice:
            pg.draw.circle(win, (200, 200, 200), point, 4)
        for line in self.edge:
            pg.draw.line(win, (200, 200, 200), line[0], line[1], 2 * (self.max_dist // line[2]))


if __name__ == '__main__':

    display_size = [1200, 900]
    window = pg.display.set_mode(display_size)

    clock = pg.time.Clock()
    run_flag = True
    graph = Graph(200, 40, 2)

    while run_flag:

        clock.tick(30)

        for eve in pg.event.get():
            if eve.type == pg.QUIT:
                run_flag = False

        graph.find_close_points()

        graph.draw(window)
        pg.display.update()
        graph.move_vertices(display_size)
