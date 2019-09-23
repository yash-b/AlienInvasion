import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.locals.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.locals.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.locals.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.locals.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.locals.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    """Respond to key releases."""
    if event.key == pygame.locals.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.locals.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

def update_screen(ai_settings, surface, ship, bullets):
    """Update images on the screen and flilp to the new screen."""
        surface.fill(ai_settings.bg_color)
        ship.blitme()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()