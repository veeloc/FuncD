#import modules
import os, sys

#define parsing functions
class funcdata():
	
	def __init__(self):
		self.systemFunctions = []
		# Default class functions

		self.systemFunctions.append(('move','T_NUM'))
		self.systemFunctions.append(('moved','T_STR','T_NUM'))
		self.systemFunctions.append(('turn','T_NUM'))
		self.systemFunctions.append(('turnl','T_NUM'))
		self.systemFunctions.append(('random',))
		self.systemFunctions.append(('randomd','T_NUM'))
		self.systemFunctions.append(('penUp',))
		self.systemFunctions.append(('penDown',))
		# List used to store local functions from parsed file
		self.localFunctions = []
	
	def getReturnTypeForFunctionName(self,funcName):
		for x in self.systemFunctions:
			if (x[0] == funcName):
				return x
				
	def addBlocks(self, blocks):
		self.localFunctions = blocks[:]
	
	def getLocalBlockByName(self, name):

		for x in self.localFunctions:
			if (x[0][0] == name):
				return x[1]
	
