import pygame
import random
pygame.init()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

#Creating Window
screen_width = 800
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Classic Snake Game!")
pygame.display.update()

#Game Specific variables



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def text_score(text, color, x, y):
	screen_text = font.render(text, True, color)
	gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
	for x,y in snk_list:
		pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])



#Game Loop
def gameloop():
	exit_game = False
	game_over = False
	snk_list = []
	snk_length = 1
	snake_x = 50
	snake_y = 50
	snake_size = 20 
	velocity_x = 0
	velocity_y = 0
	food_x = random.randint(30, screen_width/2)
	food_y = random.randint(30, screen_height/2)
	fps = 30
	score = 0
	init_velocity = 5
	with open("best.txt", "r") as f:
		highscore = f.read()
	while not exit_game:
		if game_over:
			with open("best.txt", "w") as f:
				f.write(str(highscore))
			gameWindow.fill(white)
			text_score("Game Over! Press Enter to continue", red, screen_width/2-200, screen_height/2-30)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						gameloop()     
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						velocity_x = init_velocity
						velocity_y = 0

					if event.key == pygame.K_LEFT:
						velocity_x = -1*init_velocity
						velocity_y = 0

					if event.key == pygame.K_UP:
						velocity_y = -1*init_velocity
						velocity_x = 0

					if event.key == pygame.K_DOWN:
						velocity_y = init_velocity
						velocity_x = 0

			snake_x += velocity_x
			snake_y += velocity_y

			if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
				score += 1
				if score%2 == 0:
					init_velocity += 1
				food_x = random.randint(50, screen_width-50)
				food_y = random.randint(50, screen_height-50)
				snk_length += 3
				if score > int(highscore):
					highscore = score

			gameWindow.fill(white)
			text_score("Score : "+str(score)+" HighScore : "+str(highscore), red, 5, 5)
			pygame.draw.rect(gameWindow, red, (food_x, food_y, snake_size, snake_size))

			head = []
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)

			if len(snk_list) > snk_length:
				del snk_list[0]

			if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
				game_over = True

			if head in snk_list[:-1]:
				game_over = True

			plot_snake(gameWindow, black, snk_list, snake_size)

		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	quit()

gameloop()