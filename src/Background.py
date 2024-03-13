class Background:
    #pygame import
    import pygame
    
    # Start Screen Variables

    width, height = 650, 650

    # Seal and background for the start screen
    setScreen = pygame.display.set_mode((width, height))

    loadOcean = pygame.image.load("AHwave.png")
    w, h = (loadOcean.get_width()) * (width/loadOcean.get_width()), (loadOcean.get_height()) * (height/loadOcean.get_height())
    xpos = width / 2 - (w/2)
    ypos = height / 2 - (h/2)

    oceanSize = pygame.transform.scale(loadOcean, (w, h))

    # screen.blit(sealSize, (xpos, ypos))

    # pygame.display.set_caption("Seal Game")

    # pygame.display.update()