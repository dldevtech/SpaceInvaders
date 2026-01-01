import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()

        # Configuración del color de fondo de la pantalla
        self.bg_color = (self.settings.bg_color) 

    def run_game(self):
        """Inicio del bucle principal del juego"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            # Se deshace de las balas que han desaparecido
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Responde a las pulsaciones de las teclas y eventos del ratón"""
        # Buscamos eventos del ratón y el teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Responde a las pulsaciones de las teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a las liberaciones de las teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de balas"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
            """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva"""
            self.screen.fill(self.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()

            # Hace visible la última pantalla dibujada
            pygame.display.flip()

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    si = SpaceInvader()
    si.run_game()