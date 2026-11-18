import random
import pygame
import sys

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
GREEN = "#00ff00"
SEGMENT_SIZE = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

engine = True
clock = pygame.time.Clock()
snake = [[100, 100], [90, 100], [80, 100]]
direction = [20, 0]
food = [random.randrange(0, SCREEN_WIDTH, SEGMENT_SIZE), random.randrange(0, SCREEN_HEIGHT, SEGMENT_SIZE)]

while engine:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            engine = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != [0, 20]:
                direction = [0, -20]
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != [0, -20]:
                direction = [0, 20]
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != [20, 0]:
                direction = [-20, 0]
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != [-20, 0]:
                direction = [20, 0]
            elif event.key == pygame.K_ESCAPE:
                engine = False

    screen.fill(WHITE)
    head = [snake[0][0]+direction[0], snake[0][1]+direction[1]]
    # print("snake 1", snake)
    snake.insert(0, head)
    # print("snake 2", snake)
    # print("food", food)
    if snake[0] == food:
        # print("!@#$%^&*()")
        food = [random.randrange(0, SCREEN_WIDTH, SEGMENT_SIZE), random.randrange(0, SCREEN_HEIGHT, SEGMENT_SIZE)]
    else:
        snake.pop(len(snake)-1)
        
    if (snake[0][0] == 0 or snake[0][0] == SCREEN_WIDTH) or (snake[0][1] == 0 or snake[0][1] == SCREEN_HEIGHT):
        engine = False
    for i in range(1, len(snake)):
            if snake[0] == snake[i]:
                engine = False
                break

    
    for i in range(1, len(snake)):
        pygame.draw.rect(screen, BLACK, [snake[i][0], snake[i][1], SEGMENT_SIZE, SEGMENT_SIZE])
    pygame.draw.rect(screen, GREEN, [snake[0][0], snake[0][1], SEGMENT_SIZE, SEGMENT_SIZE])
    pygame.draw.circle(screen, RED, [food[0], food[1]], SEGMENT_SIZE/2)
    pygame.display.flip()
    clock.tick(5)


pygame.quit()
sys.exit()
