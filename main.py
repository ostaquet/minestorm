import pygame

from color_palette import ColorPalette
from fire import Fire
from starship import Starship


def main():
    pygame.init()

    window_size: tuple[float, float] = (800, 600)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Minestorm")

    clock = pygame.time.Clock()

    game_over = False

    player1: Starship = Starship(window)
    shoots: list[Fire] = []

    while not game_over:
        # Event management
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoots.append(Fire(window, player1.get_pos(), player1.get_angle()))

        # Control management
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            player1.turn_left()
        if keys_pressed[pygame.K_RIGHT]:
            player1.turn_right()
        if keys_pressed[pygame.K_UP]:
            player1.boost()
        if keys_pressed[pygame.K_DOWN]:
            player1.brake()

        # Logic
        # Clean fires that don't exist anymore
        for shoot in shoots:
            if not shoot.is_exist():
                shoots.remove(shoot)

        # Draw graphics
        window.fill(ColorPalette.background)
        player1.draw()
        for shoot in shoots:
            shoot.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
