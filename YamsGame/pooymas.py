import pygame
import os

Bleu_claire = (163, 227, 255)
Bleu = (240, 240, 240)
Blanc = (240, 240, 240)
screen = pygame.display.set_mode((1080, 720))
Rectangle = ()


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.system('exit')

    def update(self):
        pass

    def display(self):
        self.screen.fill(Blanc)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(144)

pygame.init()
game = Game(screen)
game.run()

pygame.quit()
os.system('cls')