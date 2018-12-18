import pygame
import random
import time

pygame.init()

windowW = 640
windowH= 640

window = pygame.display.set_mode((windowW, windowH))
pygame.display.set_caption('simple game')

clock = pygame.time.Clock()

white = (255,255,255)
grey = (128,128,128)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

background = pygame.image.load("background.png")

def blocky(x,y,w,l,life):
	if life == False:
		pygame.draw.circle(window, red, (x + 12, y + 12), 30)

	else:
		pygame.draw.rect(window, black, [x, y, w, l])
		pygame.draw.rect(window, white, [x + 2, y + 3, 5, 5])
		pygame.draw.rect(window, white, [x + 18, y + 3, 5, 5])

def stabby(x,y,w,h,color):
	pygame.draw.rect(window, color, [x, y, w, h])

def stabby2(x,y,w,h,color):
	pygame.draw.rect(window, color, [x, y, w, h])

def slashy(x,y,w,h,color):
	pygame.draw.rect(window, color, [x, y, w, h])

def gameLoop():
	end = False

	bloc_x = 275
	bloc_y = 275
	bloc_w = 25
	bloc_h = 25

	bloc_vel = 7.5

	blocky_life = True

	stabby_startx = random.randrange(0, windowW)
	stabby_starty = -100
	stabby_speed = random.randrange(10, 20)
	stabby_width = 10
	stabby_height = 40

	stabby2_startx = random.randrange(0, windowW)
	stabby2_starty = -100
	stabby2_speed = random.randrange(10, 20)
	stabby2_width = 10
	stabby2_height = 40

	slashy_startx = -100
	slashy_starty = random.randrange(0, windowH)
	slashy_speed = random.randrange(10, 20)
	slashy_width = 40
	slashy_height = 10

	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		keys = pygame.key.get_pressed()

		if blocky_life == True:
			if keys[pygame.K_RIGHT] and bloc_x < windowW - bloc_w - bloc_vel:
				bloc_x += bloc_vel
			if keys[pygame.K_LEFT] and bloc_x > bloc_vel:
				bloc_x -= bloc_vel
			if keys[pygame.K_UP] and bloc_y > bloc_vel:
				bloc_y -= bloc_vel
			if keys[pygame.K_DOWN] and bloc_y < windowH - bloc_h - bloc_vel:
				bloc_y += bloc_vel
			if keys[pygame.K_q]:
				break

		window.fill(white)
		#window.blit(background, (0,0))

		blocky(bloc_x, bloc_y, bloc_w, bloc_h, blocky_life)

		stabby(stabby_startx, stabby_starty, stabby_width, stabby_height, grey)
		stabby_starty += stabby_speed

		stabby2(stabby2_startx, stabby2_starty, stabby2_width, stabby2_height, grey)
		stabby2_starty += stabby2_speed

		slashy(slashy_startx, slashy_starty, slashy_width, slashy_height, grey)
		slashy_startx += slashy_speed

		if stabby_starty > windowH - 20:
			stabby_starty = 0 - stabby_starty
			stabby_startx = random.randrange(0, windowW)
			stabby_speed = random.randrange(10, 20)

		if stabby2_starty > windowH - 20:
			stabby2_starty = 0 - stabby2_starty
			stabby2_startx = random.randrange(0, windowW)
			stabby2_speed = random.randrange(10, 20)

		if slashy_startx > windowW - 20:
			slashy_startx = 0 - slashy_width
			slashy_starty = random.randrange(0, windowH)
			slashy_speed = random.randrange(10, 20)

		pygame.display.update()
		clock.tick(60)

gameLoop()