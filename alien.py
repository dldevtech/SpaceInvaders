import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """Una clase para representar un solo alien en la flota"""

    def __init__(self, si_game):
        """Inicializa el alien y le establece una posición inicial"""
        super().__init__()
        self.screen = si_game.screen

        # Carga la imagen del alien y configura su atributo rect
        self.image = pygame.image.load('F:/ProyectosVS/SpaceInvaders/images/alienigena.bmp')
        
        # Reescalamos la imagen por su tamaño
        self.image = pygame.transform.scale(self.image, (80, 60))
        
        self.rect = self.image.get_rect()

        # Inicia un nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guarda la posición horizontal exacta del alien
        self.x = float(self.rect.x)
