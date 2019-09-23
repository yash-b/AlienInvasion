import sys
import pygame
from modules.settings import Settings
from modules.ship import Ship
from modules.bullets import Bullet
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    surface = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    ship = Ship(ai_settings, surface)
    # Make a group to store bullets in.
    bullets = pygame.sprite.Group()

    while True:
        gf.check_events(ai_settings, surface, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, surface, ship, bullets)


run_game()