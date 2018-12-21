import pygame
import random
import time


# I think this is super cool!!!
# Well done!
# 
# Daniel's Suggestions
# If stabby, stabby2, and slashy do the same thing (as in the code in
# their functions are the same) then you don't need three different
# functions.
# Instead, you could make a function called "makeBlock(x,y,w,h,color)"
# that you just call three times.
# Also, I'd call the function for the main character "makeMainCharacter"
# since you can choose a block (rectangle) or circle depending on the
# value of "life"
# 
# I can also probably help with getting the loop to remember all the 
# stabby bois on the screen in order to make sure that the main character
# gets hit by any stabby boi that enters the main character's hit box.
#
# Overall, fantatastic! I like the art and the idea!



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

background = pygame.image.load("background2.png")

def blocky(x,y,w,l,life):
	if life == False:
		pygame.draw.circle(window, red, (int(x + 12), int(y + 12)), 30)

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
	bloc_x = 275
	bloc_y = 275
	bloc_w = 25
	bloc_h = 25

	bloc_vel = 7.5

	blocky_life = True

	# Set the dimensions of horizontal or vertical bois
	# Ex:
	# hor_width = 40
	# hor_height = 10

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

	# Set the initial number of enemy bois
	# Ex:
	# num_enemies = 4

	# Initialize an empty list of enemies
	# Ex:
	# enemy_list = []

	while True:
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

		# Might want a way to reset the game...

		window.fill(white)
		#window.blit(background, (0,0))

		blocky(bloc_x, bloc_y, bloc_w, bloc_h, blocky_life)

		# Check if there are too few enemies.
		# If so, we update the list with new enemies until we have enough
		# Ex:
		# while len(enemy_list) < num_enemies:
		#     (Everything below should be a separate function!)
		#     select a random number
		#     if random number > 0.5, add a horizontal enemy
		#         ex: makeBox(values for horizontal and random y value)
		#         and update the list of enemy list
		#         ex: enemy_list.append((True, x, y))
		#     otherwise, add a vertical enemy
		#         similar to above


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

		# The hit box:
		# We want to go through each element in the enemy list,
		# if the block is intersecting the enemy, block is no longer alive
		# Probably just want a separate function for this.

		if bloc_y < stabby_starty + stabby_height:
			print('ye. character y value less than stabby boi y value.')

			if bloc_x > stabby_startx and bloc_x < \
			  stabby_startx + stabby_width or \
			  bloc_x + bloc_w > stabby_startx and \
			  bloc_x + bloc_w < stabby_startx + stabby_width:
				blocky_life = False

		pygame.display.update()
		clock.tick(60)

gameLoop()