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
pygame.display.set_caption('Balloon Pop')

# Inisiasi clock for FPS
fps = 30
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1920)  # width
cap.set(4, 1080)  # height

# Images
imgBalloon = pygame.image.load('../Resources/balon.png')
imgBalloon = pygame.transform.scale(imgBalloon, (imgBalloon.get_width() // 2, imgBalloon.get_height() // 2))
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = 500, 500

# Variables
speed = 15
score1 = 0  # Score for right hand (Player 1)
score2 = 0  # Score for left hand (Player 2)

StartTime = time.time()
totalTime = 20  # extend game time

detector = HandDetector(detectionCon=0.8, maxHands=2)


def reset_balloon():
    rectBalloon.x = random.randint(100, img.shape[1] - 100)
    rectBalloon.y = img.shape[0] + 50


# Main loop
start = True
while start:
    # Get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply logic
    timeRemain = int(totalTime - (time.time() - StartTime))
    if timeRemain < 0:
        window.fill((255, 255, 255))

        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 50)
        textScore1 = font.render(f'Player 1 Score (Right Hand): {score1}', True, (255, 50, 50))
        textScore2 = font.render(f'Player 2 Score (Left Hand): {score2}', True, (50, 50, 255))
        textTimeUp = font.render(f'Time Up!', True, (0, 0, 0))
        window.blit(textScore1, (450, 350))
        window.blit(textScore2, (450, 450))
        window.blit(textTimeUp, (800, 275))

    else:
        # OpenCV
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        # Move balloon
        rectBalloon.y -= speed
        if rectBalloon.y < 0:
            reset_balloon()
            speed += 2

        # Check for hands and collisions
        if hands:
            for hand in hands:
                x, y, _ = hand['lmList'][8]  # Index finger tip
                handType = hand['type']  # Right or Left Hand

                if rectBalloon.collidepoint(x, y):
                    reset_balloon()

                    # Update score based on hand type
                    if handType == "Right":  # Player 1 (Right Hand)
                        score1 += 10
                    elif handType == "Left":  # Player 2 (Left Hand)
                        score2 += 10
                    speed += 2

        # Convert image for Pygame display
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))

        # Blit balloon and scores
        window.blit(imgBalloon, rectBalloon)

        font = pygame.font.Font('../Resources/Marcellus-Regular.ttf', 30)
        textScore1 = font.render(f'Player 1 Score (Right Hand): {score1}', True, (255, 50, 50))
        textScore2 = font.render(f'Player 2 Score (Left Hand): {score2}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (0, 0, 0))
        window.blit(textScore1, (35, 35))
        window.blit(textScore2, (35, 100))
        window.blit(textTime, (500, 35))

    # Update display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)
