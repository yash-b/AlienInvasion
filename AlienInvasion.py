# Yash Bhambhani - 893409748
# Alien Invasion
# CPSC 386

import pygame
from pygame.sprite import Group
from modules.settings import Settings
from modules.game_stats import GameStats
from modules.scoreboard import Scoreboard
from modules.button import Button
from modules.ship import Ship
import modules.game_functions as gf


def run_game():
    # Game settings init
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien-Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    bg_color = (230, 230, 230)

    # Ship, bullets, and aliens init.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
