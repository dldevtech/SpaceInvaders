import pygame
from settings import Settings

class Ship:
    """Una clase para gestionar la nave"""

    def __init__(self, si_game):
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = si_game.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('F:\ProyectosVS\SpaceInvaders\images\ship.bmp')
        # Reescalamos la imagen por su tamaño
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda un valor decimal para la posición horizontal exacta de la nave
        self.x = float(self.rect.x)

        # Banderas de movimiento; comienza con una nave que no está en movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualiza la posición de la nave en función de las banderas de movimiento"""
        # Actualiza el valor x de la nave no el rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Actualiza el objeto rect de self.x
        self.rect.x = self.x
    
    def blitme(self):
        """"Dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)