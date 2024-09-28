import random

import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time

pygame.init()

# Create Window/Display

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Baloon Pop')

# inisiasi cloch for FPS
fps = 30
clock = pygame.time.Clock()

#Webcam
cap =cv2.VideoCapture(0)
cap.set(3, 1280) #witdh
cap.set(4, 720) #height

# images
imgBallon = pygame.image.load('../Resources/balon.png')
imgBallon = pygame.transform.scale(imgBallon, (imgBallon.get_width() // 2, imgBallon.get_height() // 2))
rectBalloon = imgBallon.get_rect()
rectBalloon.x, rectBalloon.y = 500,500

#variable
speed = 15
score = 0

StartTime = time.time()
totalTime = 10

detector = HandDetector(detectionCon=0.8, maxHands=1)

def resetballoon():
    rectBalloon.x = random.randint(100,img.shape[1]-100)
    rectBalloon.y = img.shape[0]+50

#main loop
start = True
while start:
    #get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    timeRemain = int(totalTime -(time.time()-StartTime))
    if timeRemain <0 :
        window.fill((255, 255, 255))

        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        textScore = font.render(f'Your Score: {score}', True, (255, 50, 50))
        textTime = font.render(f'Time Up:', True, (255, 50, 50))
        window.blit(textScore, (450,350))
        window.blit(textTime, (530, 275))

    else :
        #opencv
        success, img = cap.read() #move the balon
        img = cv2.flip(img,1)
        hands, img = detector.findHands(img, flipType=False)

        rectBalloon.y -= speed
        if rectBalloon.y < 0:
            resetballoon()
            speed+= 2

        if hands:
            hand = hands[0]
            x, y, _ = hand['lmList'][8]
            if rectBalloon.collidepoint(x,y):
                resetballoon()
                score += 10
                speed += 2


        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))

        window.blit(imgBallon, rectBalloon)

        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        textScore = font.render(f'Score: {score}', True, (255, 50, 50))
        textTime = font.render(f'Time: {timeRemain}', True, (255, 50, 50))
        window.blit(textScore, (35,35))
        window.blit(textTime, (1000, 35))


    #update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)