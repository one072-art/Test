import pygame

pygame.init()

WIDTH, HEIGH = 1200, 800
YELLOW, BLUE = (255, 255, 0), (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGH))

button_rect = pygame.Rect(0, 0, 500, 100)
button_rect.center = (WIDTH//2, HEIGH//2)

scene_button_rect = pygame.Rect(0, 0, 900, 120)
scene_button_rect.center = (WIDTH//2, HEIGH//2 + 160)

font = pygame.font.Font(None, 64)

score = 0
scene = ''
while True:
    screen.fill(YELLOW)

    mouse_pos = pygame.mouse.get_pos()
    hovered = button_rect.collidepoint(mouse_pos)
    scene_hovered = scene_button_rect.collidepoint(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if hovered and event.type == pygame.MOUSEBUTTONDOWN:
            score += 1

        if scene_hovered and event.type == pygame.MOUSEBUTTONDOWN:
            scene = 'scene_1'

    if hovered:
        button_color = (100, 255, 100)
    else:
        button_color = BLUE

    pygame.draw.rect(screen, button_color, button_rect)
    label = font.render("CLICK", True, YELLOW)
    screen.blit(label, label.get_rect(center=button_rect.center))

    pygame.draw.rect(screen, BLUE, scene_button_rect)
    scene_label = font.render("NEXT PAGE", True, YELLOW)
    screen.blit(scene_label, scene_label.get_rect(center=scene_button_rect.center))

    score_text = font.render("SCORE: " + str(score), True, BLUE)
    screen.blit(score_text, (30, 30))

    if scene == 'scene_1':
        screen.fill(YELLOW)

    pygame.display.update()

