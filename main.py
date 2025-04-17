import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Pinball Ring Road Game!')
running = True

active_piece = None
pieces = []
for i in range(10):
    x = random.randint(50, 700)
    y = random.randint(50, 350)
    w = 70
    h = 70
    piece = pygame.Rect(x, y, w, h)
    pieces.append(piece)

while running:
    screen.fill((75, 79, 76))
    for piece in pieces:    
        pygame.draw.rect(screen, "red", piece)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()