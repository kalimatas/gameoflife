import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self, color, initial_position, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([size, size])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position