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
    red, green, blue = (255, 0, 0), (0,255,0), (0,0,255)
    pygame.draw.polygon(window, red, ((491,100),(788,100),(937,357),(788,641),(491,614),(342,357)))
    pygame.draw.circle(window,green,(640, 360),200)
    pygame.draw.line(window,blue,(463,392),(812,392), 10)
    pygame.draw.rect(window,blue,(468,307,345,70), border_radius=50)


    #update Display
    pygame.display.update()
    #set FPS
    clock.tick(fps)