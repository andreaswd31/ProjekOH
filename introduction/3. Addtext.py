import pygame

pygame.init()

# Create Window/Display

width, height = 1280, 720
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
    window.fill((255, 255, 255))
    font =pygame.font.Font('../Resources/Marcellus-Regular.ttf',100)
    text = font.render('Baloon Games', True, (50, 50, 50))
    window.blit(text, (350,300))

    #update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)