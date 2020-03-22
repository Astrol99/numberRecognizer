import pygame
import numpy as np
from tensorflow import keras

FPS = 144
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

def process_data():
    pass

# Get model
model = keras.models.load_model('MNIST.h5')
print("[+] Loaded model -> MNIST.h5")

pygame.init()

screen = pygame.display.set_mode((644, 476))
screen.fill(WHITE)

clock = pygame.time.Clock()

mainloop = True
continous_circle = False

while mainloop:
    ms = clock.tick(FPS)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if continous_circle == True:
        pygame.draw.circle(screen, BLACK, (mouse_x, mouse_y), 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

        # Main drawing controls
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if (mouse_x >= 10 and mouse_x <= 634) and (mouse_y >= 10 and mouse_y <= 466):
                pygame.draw.circle(screen, BLACK, (mouse_x, mouse_y), 10)
                continous_circle = True

        elif event.type == pygame.MOUSEBUTTONUP:
            continous_circle = False

            # Run Model
            predictions = model.predict(img)
            print(np.argmax(predictions[0]))


        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, WHITE, ((0, 0), (634, 466)))

    text = f"FPS: {clock.get_fps()}"
    pygame.display.set_caption(text)

    pygame.display.update()

pygame.quit()