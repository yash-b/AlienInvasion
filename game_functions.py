import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.locals.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.locals.KEYUP:
            if event.key == pygame.locals.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.locals.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, surface, ship):
    """Update images on the screen and flilp to the new screen."""
        surface.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()