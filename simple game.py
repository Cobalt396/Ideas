import pygame
pygame.init()

windowW = 640
windowL= 640

window = pygame.display.set_mode((windowW, windowL))
pygame.display.set_caption('simple game')

clock = pygame.time.Clock()

white = (255,255,255)
grey = (128,128,128)
black = (0,0,0)
