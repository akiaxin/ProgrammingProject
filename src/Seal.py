class Seal:
    #pygame import
    import pygame
    from Background import Background
    # Start Screen Variables

    width, height = Background.width, Background.height
    backgroundColor = 33, 33, 33
    xpos = width / 2
    ypos = height / 2

    # Seal and background for the start screen

    loadSeal = pygame.image.load("AHseal.png")
    loadSadSeal = pygame.image.load("AHSadSeal.png")
    loadSurprisedSeal = pygame.image.load("AHSurprisedSeal.png")
    w = loadSeal.get_width()
    h = loadSeal.get_height()

    xpos = width / 2 - (w * 4 / 2)
    ypos = height / 2 - (h * 4 / 2)

    sealSize = pygame.transform.scale(loadSeal, (w * 4, h * 4))
    sadSealSize = pygame.transform.scale(loadSadSeal, (w * 4, h * 4))
    surprisedSealSize = pygame.transform.scale(loadSurprisedSeal, (w * 4, h * 4))

    # screen.blit(sealSize, (xpos, ypos))

    # pygame.display.set_caption("Seal Game")

    # pygame.display.update()