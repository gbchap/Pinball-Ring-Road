import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('Pinball Ring Road Game!')
background = pygame.image.load('assets/background.png')
running = True

active_piece = None

#pieces class
class Piece:
    def __init__(self, type, image, position):
        self.type = type
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=position)
        
    def move_ip(self, rel):
        self.rect.move_ip(rel)


pieces = []

for i in range(3):
    x = random.randint(978, 1120)
    y = random.randint(153, 420)
    piece = Piece("blue", "assets/pieces/blue.png", (x, y))
    pieces.append(piece)
    
    x = random.randint(978, 1120)
    y = random.randint(153, 420)
    piece = Piece("pink", "assets/pieces/pink.png", (x, y))
    pieces.append(piece)

for i in range(2):
    x = random.randint(978, 1120)
    y = random.randint(153, 420)
    piece = Piece("yellow", "assets/pieces/yellow.png", (x, y))
    pieces.append(piece)
    
    x = random.randint(978, 1120)
    y = random.randint(153, 420)
    piece = Piece("orange", "assets/pieces/orange.png", (x, y))
    pieces.append(piece)


while running:
    screen.blit(background, (0,0))
    #screen.fill((205,186,244))
    for piece in pieces:    
        screen.blit(piece.image, piece.rect)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, piece in enumerate(pieces):
                    if piece.rect.collidepoint(event.pos):
                        active_piece = num

        if event.type == pygame.MOUSEMOTION:
            #print(event)
            if active_piece != None:
                pieces[active_piece].move_ip(event.rel)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_piece = None
    #basics:            
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
    clock.tick(60)
pygame.quit()