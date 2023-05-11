import pygame
pygame.init()

win = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surf = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surf = pygame.image.load("graphics/ground.png").convert_alpha()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(700, 300))

score = pygame.font.Font("font/Pixeltype.ttf", 50)
score_surf = score.render("Runner", False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

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
    pygame.draw.rect(win, "#c0e8ec", score_rect)
    pygame.draw.rect(win, "#c0e8ec", score_rect, 10)
    win.blit(score_surf, score_rect)

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
