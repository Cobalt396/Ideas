import pygame
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

def gameLoop():
	end = False

	bloc_x = 275
	bloc_y = 275
	bloc_w = 25
	bloc_h = 25

	bloc_vel = 5

	blocky_life = True

	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT] and bloc_x < windowW - bloc_w - bloc_vel:
			bloc_x += bloc_vel
		if keys[pygame.K_LEFT] and bloc_x > bloc_vel:
			bloc_x -= bloc_vel
		if keys[pygame.K_UP] and bloc_y > bloc_vel:
			bloc_y -= bloc_vel
		if keys[pygame.K_DOWN] and bloc_y < windowH - bloc_h - bloc_vel:
			bloc_y += bloc_vel
		if keys[pygame.K_q]:
			blocky_life = False

		window.fill(white)
		#window.blit(background, (0,0))

		blocky(bloc_x, bloc_y, bloc_w, bloc_h, blocky_life)

		pygame.display.update()
		clock.tick(60)

gameLoop()