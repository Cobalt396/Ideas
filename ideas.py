import pygame
pygame.init()

windowW = 640
windowL= 640

window = pygame.display.set_mode((windowW, windowL))
pygame.display.set_caption('ideas')

clock = pygame.time.Clock()

white = (255,255,255)
grey = (128,128,128)
black = (0,0,0)

botFront = pygame.image.load('simpleBotFront.png')
botBack = pygame.image.load('simpleBotBack.png')
botLeft = pygame.image.load('simpleBotL.png')
botRight = pygame.image.load('simpleBotR.png')

def botF(x,y):
    window.blit(botFront, (x,y))

def botB(x,y):
    window.blit(botBack, (x,y))

def botL(x,y):
    window.blit(botL, (x,y))

def botR(x,y):
    window.blit(botR, (x,y))

def gameLoop():
    end = False

    botx = 320
    boty = 320

    botx_change = 0
    boty_change = 0

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    botx_change += 5
                elif event.key == pygame.K_LEFT:
                    botx_change += -5
                elif event.key == pygame.K_DOWN:
                    boty_change += 5
                elif event.key == pygame.K_UP:
                    boty_change += -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or\
                   event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    botx_change = 0
                    boty_change = 0
                
                
        window.fill(black)

        botx += botx_change
        boty += boty_change

        botF(botx, boty)

        pygame.display.update()
        clock.tick(60)

gameLoop()
