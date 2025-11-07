import pygame

class Ship:
    """Una clase para gestionar la nave"""

    def __init__(self, si_game):
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('F:\ProyectosVS\SpaceInvaders\images\ship.bmp')
        # Reescalamos la imagen por su tamaño
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect()

        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        # Bandera de movimiento; empieza con una bandera que no se mueve
        self.moving_right = False
    
    def update(self):
        """Actualiza la posición de la nave en función de la bandera de movimiento"""
        if self.moving_right:
            self.rect.x += 1
    
    def blitme(self):
        """"Dibuja la nave en su ubicación actual"""
        self.screen.blit(self.image, self.rect)