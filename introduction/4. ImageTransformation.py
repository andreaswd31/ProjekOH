import pygame

pygame.init()

# Create Window/Display

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Baloon Games')

# inisiasi cloch for FPS
fps = 30
clock = pygame.time.Clock()

#load image
imgBackground = pygame.image.load('../Resources/BackgroundBlue.jpg').convert()
imgbalon = pygame.image.load('../Resources/balon.png').convert_alpha()
#imgbalon = pygame.transform.rotate(imgbalon, 90)
imgbalon = pygame.transform.rotozoom(imgbalon, 0,0.3)
#imgbalon = pygame.transform.flip(imgbalon, True, False)



#main loop
start = True
while start:
    #get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    #imgbalon = pygame.transform.scale(imgbalon, (50,100))
    #imgbalon = pygame.transform.smoothscale(imgbalon, (50, 100))

    window.blit(imgBackground, (0, 0))
    window.blit(imgbalon, (0,0))

    #update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)