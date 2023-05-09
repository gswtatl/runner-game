import pygame
pygame.init()

win = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("graphics/player
text = pygame.font.Font("font/Pixeltype.ttf", 50)


def main():
    clock = pygame.time.Clock()
    run = True
    snail_x_pos = 700

    while run:
        clock.tick(60)

        win.blit(sky_surface, (0, 0))
        win.blit(ground_surface, (0, 300))
        win.blit(text.render("Runner", False, (0, 0, 0)), (345, 70))
        snail_x_pos -= 4
        if snail_x_pos < -100:
            snail_x_pos = 900
        win.blit(snail_surface, (snail_x_pos, 265))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
