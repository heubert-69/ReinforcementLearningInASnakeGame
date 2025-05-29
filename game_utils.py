import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

#initialize pygame
pygame.init()
font = pygame.font.SysFont('arial', 25)


class Direction(Enum):
	right = 1
	left = 2
	up = 3
	down = 4

#X and Y coordinates for tracking
Point = namedtuple("Point", "x y")

WHITE = (255, 255, 255) #hex values of the UI
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 80
def _update_ui(self):
	self.display.fill(BLACK)
	for pt in self.snake:
		pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
		pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))
	pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
	text = font.render("Score: " + str(self.score), True, WHITE)
	self.display.blit(text, [0, 0])
	pygame.display.flip()
#setting up the dimensions of the screen
def __init__(self, w=640, h=480):
	self.w=w
	self.h=h
	self.display = pygame.display.set_mode((self.w, self.h))
	pygame.display.set_caption("Snake")
	self.clock = pygame.time.Clock()
	self.reset()
def reset(self): #game state (also include the score, food and condition of the game..duh the snake bro) if user gets hit onto any part of its body or wall
	self.direction = Direction.right
	self.head = Point(self.w / 2, self.h / 2)
	self.snake = [self.head, Point(self.head.x - BLOCK_SIZE, self.head.y), Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
	self.score = 0
	self.food = None
	self._place_food()
	self.frame_iteration = 0
def _place_food(self):
	x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
	y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
	self.food = Point(x, y)
	if self.food in self.snake:
		self._place_food()

#checking Collisions if the player crashed into a wall 
def is_collision(self, pt=None):
	#pt is the representation of the snakes head
	if pt is None:
		pt = self.head
	elif pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y  > self.h - BLOCK_SIZE or pt.y < 0:
		return True #if the snake's head hits the sides
	elif pt in self.snake[1:]:
		return True
	return False


#Actual Playing Process
def play_step(self, action):
	self.frame_iteration += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	self._move(action)
	self.snake.insert(0, self.head)
	reward = 0
	game_over = False
	if self.is_collision() or self.frame_iteration > 100 * len(self.snake): #snake is way too long or activates the is_collision function
		game_over = True
		reward = -10
		return reward, game_over, self.score
	if self.head == self.food:
		self.score += 1
		reward = -10
		self._place_food()
	else:
		self.snake.pop()
	self._update_ui()
	self.clock.tick(SPEED)
	return reward, game_over, self.score

#ensuring the snake can move in all 4 directions
def _move(self):
	clock_wise = [Direction.right, Direction.left, Direction.up, Direction.down]
	idx = clock_wise.index(self.direction)
	if np.array_equal(action, [1, 0, 0]):
		#straight
		new_dir = clockwise[idx]
	elif np.array_equal(action, [0, 1, 0]): #right
		next_idx = (idx + 1) % 4
		new_dir = clock_wise[next_idx]
	else: #left turn or [0, 0, 1]
		next_idx = (idx - 1) % 4
		new_dir = clock_wise[next_idx]
	self.direction = new_dir

	x = self.head.x
	y = self.head.y

	if self.direction == Direction.right:
		x += BLOCK_SIZE
	elif self.direction == Direction.left:
		x -= BLOCK_SIZE
	elif self.direction == Direction.up:
		y -= BLOCK_SIZE
	elif self.direction == Direction.down:
		y += BLOCK_SIZE
	self.head = Point(x, y)
