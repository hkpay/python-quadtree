import pygame
import sys
import random
import math

from quadtree import QTreePartition, PointQTreeNode

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

POINTS_COUNT = 50
POINT_RADIUS = 1
POINT_SPAWN_AREA_SIZE = (SCREEN_SIZE[0] - 20, SCREEN_SIZE[1] - 20)
POINT_SPAWN_AREA_MIN = (10, 10)
POINT_SPAWN_AREA_MAX = (POINT_SPAWN_AREA_MIN[0] + POINT_SPAWN_AREA_SIZE[0], POINT_SPAWN_AREA_MIN[1] + POINT_SPAWN_AREA_SIZE[1])

def generate_random_points(points_count):
    points = []

    for _ in range(points_count):
        coord = ( random.randint(POINT_SPAWN_AREA_MIN[0], POINT_SPAWN_AREA_MAX[0]), random.randint(POINT_SPAWN_AREA_MIN[1], POINT_SPAWN_AREA_MAX[1]) ) 
        keep = True
        for point in points:
            keep = keep and (math.dist(coord, point) > POINT_RADIUS * 2)
        if keep:
            points.append(coord)

    return points

def draw_qtree_node(qtreenode, surface):
    rect = pygame.Rect(qtreenode.partition.x,qtreenode.partition.y, qtreenode.partition.w, qtreenode.partition.h)
    pygame.draw.rect(surface, RED, rect, 1)

def draw_qtree(qtreenode, surface):
    draw_qtree_node(qtreenode, surface)
    for child in qtreenode.children:
        draw_qtree(child, surface)

def build_qtree_root(topleftcorner, size, points = []):
    qtreeroot = PointQTreeNode(QTreePartition(topleftcorner[0], topleftcorner[1], size[0], size[1]))
    for point in points:
        qtreeroot.insert(point)
    return qtreeroot

def main():
    pygame.init()
    
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Point Quadtree")
    clock = pygame.time.Clock()

    points = generate_random_points(POINTS_COUNT)
    
    qtree = build_qtree_root(POINT_SPAWN_AREA_MIN, POINT_SPAWN_AREA_SIZE, points)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    points = generate_random_points(POINTS_COUNT)
                    qtree = build_qtree_root(POINT_SPAWN_AREA_MIN, POINT_SPAWN_AREA_SIZE, points)
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill(BLACK)
        draw_qtree(qtree, screen)
        for point in points:
            pygame.draw.circle(screen, WHITE, point, POINT_RADIUS, 1)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

