import pygame
import pygame.freetype
import numpy as np
from tensorflow import keras
from PIL import Image
import os

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

pygame.freetype.init()
FONT_BIG = pygame.freetype.Font("Resources/OpenSans-Light.ttf", 36)
FONT_SMALL = pygame.freetype.Font("Resources/OpenSans-Light.ttf", 24)

# Get model
model = keras.models.load_model('MNIST.h5')
print("[+] Loaded model -> MNIST.h5")

pygame.init()

screen = pygame.display.set_mode((900, 466))
screen.fill(BLACK)

pygame.display.set_caption("Number Recognizer")

# Temporary folder to store images
if os.path.isdir("img_tmp") == False:
    os.mkdir("img_tmp")

def process_data():
    rect = pygame.Rect((0,0), (634, 466))
    sub = screen.subsurface(rect)
    pygame.image.save(sub, "img_tmp/screenshot.jpg")

    img = Image.open("img_tmp/screenshot.jpg")
    img = img.resize((28,28), Image.ANTIALIAS)

    array = np.asarray(img)
    array = array / 255.0
    array = array[:, :, 0]
    array = (np.expand_dims(array, 0))

    img.save("img_tmp/postprocess.jpg")

    return array

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

# Render Text
FONT_BIG.render_to(screen, (695, 80), "Prediction", WHITE)
FONT_BIG.render_to(screen, (700, 300), "Accuracy", WHITE)

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
            result = str(np.argmax(predictions[0]))
            accuracy = np.max(predictions[0])
            accuracy = round(float(accuracy), 3)   # Round to nearest hundreath place

            pygame.draw.rect(screen, BLACK, ((760, 135), (100, 50)))
            pygame.draw.rect(screen, BLACK, ((735, 350), (200, 50)))

            FONT_SMALL.render_to(screen, (760, 135), result, WHITE)
            FONT_SMALL.render_to(screen, (735, 350), str(accuracy*100) + "%", WHITE)

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, BLACK, ((0, 0), (645, 466)))

    pygame.display.update()

pygame.quit()