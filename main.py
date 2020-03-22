import pygame

FPS = 30
playtime = 0.0
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

pygame.init()

screen = pygame.display.set_mode((640, 480))
screen.fill(WHITE)

clock = pygame.time.Clock()

mainloop = True
continous_circle = False

while mainloop:
    ms = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

        # Main drawing controls
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if (mouse_x >= 10 and mouse_x <= 630) and (mouse_y >= 10 and mouse_y <= 470):
                pygame.draw.circle(screen, BLACK, (mouse_x, mouse_y), 10)

        elif event.type == pygame.MOUSEBUTTONUP:
            pass

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, WHITE, ((0, 0), (640, 480)))

    text = f"FPS: {clock.get_fps()}"
    pygame.display.set_caption(text)

    pygame.display.update()

pygame.quit()