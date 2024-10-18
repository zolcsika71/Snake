import pygame
from game.game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    game.snake.direction = event.key

        if not game.update():
            running = False

        game.draw(screen)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    print(f"Game Over! Score: {game.score}")

if __name__ == '__main__':
    main()
