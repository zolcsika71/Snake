import pygame

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = pygame.K_RIGHT

    def move(self):
        head = self.body[0]
        x, y = head
        if self.direction == pygame.K_UP:
            new_head = (x, y - 10)
        elif self.direction == pygame.K_DOWN:
            new_head = (x, y + 10)
        elif self.direction == pygame.K_LEFT:
            new_head = (x - 10, y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (x + 10, y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        return len(self.body) != len(set(self.body))

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))
