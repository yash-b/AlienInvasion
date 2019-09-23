import sys
import pygame
from modules.settings import Settings
from modules.ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    surface = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    ship = Ship(surface)

    while True:
        gf.check_events()

        surface.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()