import pygame
import sys
import random
import math

from quadtree import QTreeNode

SCREEN_MARGIN = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

POINTS_COUNT = 1000
POINT_RADIUS = 10

def generate_random_points(points_count):
    points = []

    for i in range(points_count):
        coord = ( random.randint(SCREEN_MARGIN, SCREEN_WIDTH - SCREEN_MARGIN), random.randint(SCREEN_MARGIN, SCREEN_HEIGHT - SCREEN_MARGIN) ) 
        keep = True
        for point in points:
            keep = keep and (math.dist(coord, point) > POINT_RADIUS * 2)
        if keep:
            points.append(coord)

    return points

def main():
    pygame.init()
    
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Point Quadtree")
    clock = pygame.time.Clock()

    points = generate_random_points(POINTS_COUNT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    points = generate_random_points(POINTS_COUNT)
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill(BLACK)
        for point in points:
            pygame.draw.circle(screen, WHITE, point, POINT_RADIUS, 1)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

