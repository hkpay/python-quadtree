import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
FPS = 60

BLACK = (0, 0, 0)
WHITE = (1, 1, 1)

def main():
    pygame.init()
    
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Point Quadtree")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, SCREEN_CENTER, 10)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

    


if __name__ == "__main__":
    main()

