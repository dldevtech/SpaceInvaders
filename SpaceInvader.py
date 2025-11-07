import sys

import pygame

from settings import Settings
from ship import Ship

class SpaceInvader:
    """Clase general que gestionará los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inicializa el juego y crea los recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings ()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("SpaceInvaders")

        self.ship = Ship(self)

        # Configuración del color de fondo de la pantalla
        self.bg_color = (self.settings.bg_color) 

    def run_game(self):
        """Inicio del buble principal del juego"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Responde a las pulsaciones delas teclas y eventos del ratón"""
        # Buscamos eventos del ratón y el teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
            """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva"""
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            # Hace visible la última pantalla dibujada
            pygame.display.flip()

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    si = SpaceInvader()
    si.run_game()