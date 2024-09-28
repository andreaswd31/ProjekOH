import pygame

pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Baloon Games')

# inisiasi clock for FPS
fps = 30
clock = pygame.time.Clock()

# load image
imgBackground = pygame.image.load('../Resources/BackgroundBlue.jpg').convert()
imgbalon = pygame.image.load('../Resources/balon.png').convert_alpha()

imgbalon = pygame.transform.scale(imgbalon, (imgbalon.get_width() // 2, imgbalon.get_height() // 2))
rectBallon = imgbalon.get_rect()

# rect
rectNew = pygame.Rect(500,0,200,200)


# main loop
start = True
while start:
    # get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    rectBallon.colliderect(rectNew)
    rectBallon.x += 5  # move right


    # update display
    window.blit(imgBackground, (0, 0))
    #pygame.draw.rect(window, (0, 255, 0), rectNew)

    window.blit(imgbalon, rectBallon)

    pygame.display.update()
    clock.tick(fps)
