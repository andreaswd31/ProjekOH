import pygame

pygame.init()

# Create Window/Display

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Baloon Games')

# inisiasi cloch for FPS
fps = 30
clock = pygame.time.Clock()

#main loop
start = True
while start:
    #get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # apply logic
    window.fill((255, 0, 0))

    #update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)