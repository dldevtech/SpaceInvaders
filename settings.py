class Settings:
    """Unna clase para guardar toda la configuración de SpaceInvaders"""

    def __init__(self):
        """Inicialización de la configuración del juego"""
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 50)

        # Configuración de la nave
        self.ship_speed = 2

        # Configuración de las balas
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color = (255, 20, 147)
        self.bullets_allowed = 4