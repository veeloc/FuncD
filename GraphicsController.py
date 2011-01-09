#import modules
import pygame, os, sys, math, random

#define drawing functions
class graphicscontroller():
	
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((500,500))
		pygame.display.set_caption("FuncD", "FuncD")
		
		#define private variables with defaults
		self.x = 0 # x-co
		self.y = 0 # y-co
		self.w = 5 # width
		self.a = 0 # angle
		self.last = [self.x, self.y] # last coordinates drawn
		self.color = pygame.Color(255, 255, 255)
		self.pen = False
		self.screen = pygame.display.get_surface()

	def update(self):
		pygame.display.flip()
	
	# Main Drawing Methods For GC
	''' Moves the pen lengthToMove space'''
	def move(self, _len):
		
		_len = int(_len)
		
		x = _len*math.sin(self.a*(math.pi/180))
		y = math.fabs(_len*math.cos(self.a*(math.pi/180)))
		
		if (x < 0):
			self.x = self.last[0]-x
			self.y = self.last[1]-y
		else:
			self.x = x + self.last[0]
			self.y = y + self.last[1]
			
		
		self.x = _len*math.sin(self.a*(math.pi/180)) + self.last[0]
		if (self.pen == False):
			pygame.draw.line(self.screen, self.color, self.last, (self.x, self.y), self.w)
		self.last = [self.x, self.y]
		
		pygame.display.flip()
			
	def moved(self, _dir, _len):
		
		_len = int(_len)
		
		if (_dir == 'right' or _dir == 'r'): self.a = 90
		elif (_dir == 'down' or _dir == 'd'): self.a = 180
		elif (_dir == 'left' or _dir == 'l'): self.a = 270
		elif (_dir == 'up' or _dir == 'u'): self.a = 0
		
		self.move(_len)
		
	def turn(self, amount):
		amount = int(amount)
		self.a = self.a + amount
	#	if (self.a > 360): self.a = 360 - self.a
		
	def turn_l(self, amount):
		amount = int(amount)
		self.a = self.a - amount
	#	if (self.a < 0): self.a = 360 - math.fabs(self.a)
	
	def random(self):
		self.turn(random.randint(0,360))
		
	def randomd(self, _len):
		self.turn(random.randint(0,360))
		self.move(_len)
	
	''' Puts the Pen Up'''
	def penUp(self):
		self.pen = True
	''' Puts the Pen Down'''
	def penDown(self):
		self.pen = False
		
		