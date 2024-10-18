import pygame
from .snake import Snake
from .food import Food

class Game:
    def __init__(self):
        self.width = 400
        self.height = 400
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.position = self.food.randomize_position()
            self.score += 1
        
        if (self.snake.check_collision() or 
            self.snake.body[0][0] < 0 or self.snake.body[0][0] >= self.width or
            self.snake.body[0][1] < 0 or self.snake.body[0][1] >= self.height):
            return False
        return True

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.snake.draw(surface)
        self.food.draw(surface)
