import pygame
import RPi.GPIO as GPIO
import subprocess

count = 1;
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.wait_for_edge(3, GPIO.FALLING)

while count != 4:
    pygame.init()

    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # assigning values to X and Y variable
    X = 400
    Y = 400

    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Monitor ' + str(count))

    font = pygame.font.Font('freesansbold.ttf', 32)

    # create a text suface object,
    # on which text is drawn on it.
    text = font.render('Este es el monitor ' + str(count), True, green, blue)

    textRect = text.get_rect()

    # set the center of the rectangular object.
    # textRect.center = (X // 2, Y // 2)

    display_surface.fill(black)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();  # sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                print("Hey, you pressed the key, '0'!")
                pygame.quit()
                quit()
            if event.key == pygame.K_1:
                print("Doing whatever")

    pygame.display.update()

    GPIO.wait_for_edge(3, GPIO.FALLING)
    count = count + 1

pygame.quit()

