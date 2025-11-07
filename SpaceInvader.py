import sys

import pygame

class SpaceInvader:
    """Clase general que gestionará los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inicializa el juego y crea los recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("SpaceInvaders")

        # Configuración del color de fondo de la pantalla
        self.bg_color = (50,50,50) 

    def run_game(self):
        """Inicio del buble principal del juego"""
        while True:
            # Buscamos eventos del ratón y el teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redibuja la pantalla en cada paso por el bucle
            self.screen.fill(self.bg_color)

            # Hace visible la última pantalla dibujada
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    si = SpaceInvader()
    si.run_game()