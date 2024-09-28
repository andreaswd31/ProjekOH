import pygame
import cv2
import numpy as np


pygame.init()

# Create Window/Display

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Baloon Games')

# inisiasi cloch for FPS
fps = 30
clock = pygame.time.Clock()

#Webcam
cap =cv2.VideoCapture(0)
cap.set(3, 1280) #witdh
cap.set(4, 720) #height

#main loop
start = True
while start:
    #get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic

    #opencv
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame = pygame.transform.flip(frame, True, False)
    window.blit(frame, (0, 0))

    #update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)