import pygame
import numpy as np
from tensorflow import keras
from PIL import Image

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
#FONT = pygame.font.Font

# Get model
model = keras.models.load_model('MNIST.h5')
print("[+] Loaded model -> MNIST.h5")

pygame.init()

screen = pygame.display.set_mode((800, 466))
screen.fill(BLACK)

pygame.display.set_caption("Number Recognizer")

def process_data():
    rect = pygame.Rect((0,0), (634, 466))
    sub = screen.subsurface(rect)
    pygame.image.save(sub, "screenshot.jpg")

    img = Image.open("screenshot.jpg")
    img = img.resize((28,28), Image.ANTIALIAS)

    array = np.asarray(img)
    array = array / 255.0
    array = array[:, :, 0]
    array = (np.expand_dims(array, 0))

    return array

# Create line between drawing and info
pygame.draw.line(screen, WHITE, (640, 0), (640, 466))

"""
def process_data():
    array = pygame.surfarray.array2d(screen)
    array = np.resize(array, (28,28))
    array = array / 255.0
    array = np.expand_dims(array, 0)
    print(array.size)
    return array
"""

mainloop = True
continous_circle = False

while mainloop:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if continous_circle == True:
        if (mouse_x >= 10 and mouse_x <= 634) and (mouse_y >= 10 and mouse_y <= 466):
            pygame.draw.circle(screen, WHITE, (mouse_x, mouse_y), 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

        # Main drawing controls
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if (mouse_x >= 10 and mouse_x <= 634) and (mouse_y >= 10 and mouse_y <= 466):
                pygame.draw.circle(screen, WHITE, (mouse_x, mouse_y), 10)
                continous_circle = True

        elif event.type == pygame.MOUSEBUTTONUP:
            continous_circle = False

            # Run Model
            predictions = model.predict(process_data())
            print(np.argmax(predictions[0]))
            print(np.max(predictions[0]))

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, BLACK, ((0, 0), (640, 466)))

    pygame.display.update()

pygame.quit()
