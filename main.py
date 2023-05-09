import pygame
pygame.init()

win = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surf = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surf = pygame.image.load("graphics/ground.png").convert_alpha()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(700, 300))

text = pygame.font.Font("font/Pixeltype.ttf", 50)

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision")

    clock.tick(60)

    win.blit(sky_surf, (0, 0))
    win.blit(ground_surf, (0, 300))
    win.blit(text.render("Runner", False, (0, 0, 0)), (345, 70))

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    win.blit(snail_surf, snail_rect)

    win.blit(player_surf, player_rect)

    # if player_rect.colliderect(snail_rect) == 1:
    #     print("Collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
