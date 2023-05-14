import pygame


def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    win.blit(score_surf, score_rect)


pygame.init()
win = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True
start_time = 0

sky_surf = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surf = pygame.image.load("graphics/ground.png").convert_alpha()

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(700, 300))

# score_surf = test_font.render("Runner", False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(400, 50))

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand_rect = player_stand.get_rect(center=(400, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)

    if game_active:
        win.blit(sky_surf, (0, 0))
        win.blit(ground_surf, (0, 300))
        # pygame.draw.rect(win, "#c0e8ec", score_rect)
        # pygame.draw.rect(win, "#c0e8ec", score_rect, 10)
        # win.blit(score_surf, score_rect)
        display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        win.blit(snail_surf, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        win.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        win.fill((94, 129, 162))
        win.blit(player_stand, player_stand_rect)

    pygame.display.update()
    clock.tick(60)
