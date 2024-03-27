import pygame
pygame.init()

pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("My first pygame program")
# pygame.display.set_icon(pygame.image.load("app.bmp"))

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # pygame.quit()

    clock.tick(FPS)  # (FPS) The Loop while, runs 60 times per second
