#import modules
import os, sys, time, string
from FuncData import *
from GraphicsController import *

#define parsing functions
class funcdinterpreter():
	#options: the build options from the makefile
	
	def __init__(self):
		self.gcStarted = False
		self.db = funcdata()
	def startGC(self):
		#initialize GC
		self.gc = graphicscontroller()
		self.gcStarted = True
		
	def tokenize(self, inputStr):
		
		#define tokens dictionary
		tokenDict = {'[': 'T_OPENBRAK', ']': 'T_CLOSEBRAK',
	                  '(': 'T_OPENPAR', ')':  'T_CLOSEPAR',
	                  ';':  'T_SEMIC', ',': 'T_COM',
						':' : 'T_COL'}
	
		if (len(sys.argv) > 1):
			if (sys.argv[1] == '-t'):
				t0 = time.time()

		tokens = []
		# Loop over every character and begin to tokenize
		pos = 0
		
		while (pos < len(inputStr)):
			
			x = inputStr[pos]
			t = 'T_NULL'
			
			# Test for numbers
			if x in string.digits:
				t = 'T_NUM'
				next = self.nextCh(inputStr, pos)	
				if next in string.digits:
					pos += 1
					temp = inputStr[pos]
					while temp in string.digits and pos < len(inputStr):
						x += temp
						pos += 1
						if (pos < len(inputStr)):
							temp = inputStr[pos]
						else:
							break
					pos -= 1
						
			# Test for special characters
			elif x == '/':
				if (self.nextCh(inputStr, pos) == '/'):
					t = 'T_COMMENT'
					pos += 1
					temp = inputStr[pos]
					while temp != '\n':
						temp = inputStr[pos]
						pos += 1
						
				else:
					t = 'T_UNKNOWN'
			elif x in tokenDict:
				t = tokenDict[x]
			elif x == '>':
				t = 'T_V'
				if (self.nextCh(inputStr, pos) == '>'):
					t = 'T_VV'
					pos += 1
					temp = inputStr[pos]
				
			elif x in string.letters:
				
				t = 'T_STR'
				next = self.nextCh(inputStr, pos)
				if next in string.letters:
					pos += 1
					temp = inputStr[pos]
					while temp in string.letters and pos<len(inputStr):
						x += temp
						pos += 1
						if (pos < len(inputStr)):
							temp = inputStr[pos]
						else:
							break
					pos -= 1
				
			elif x == '\n':
				t = 'T_LNBRK'
			elif x == ' ':
				pos += 1
				continue
			else:
				# unknown
				t = 'T_UNKNOWN'
				print "[-] Unknown symbol encountered: " + x + " at position: " + str(pos+1)
			
			# End of one token
			pos += 1
			tokens.append((t,x))
			
		# End of token loop
		
		# Time options
		if (len(sys.argv) > 1):
			if (sys.argv[1] == '-t'):
				print time.time()-t0
	
		return tokens
	# End of Tokenize()
	
	def createBlocks(self, tokens):
		print "[*] Parsing blocks..."
		blocks = []
		
		pos = 0
		t = 0
		v = 1
		
		while (pos < len(tokens)):
			# Handle string tokens
			if (tokens[pos][t] == 'T_STR'):
				# Handle new tokens
				if (tokens[pos][v] == 'new'):
					pos+=1
					blockName = [tokens[pos][v]]
					pos+=3	# skip colon and \n
					lineList = []
					while(tokens[pos][t] != 'T_SEMIC'):
						tokensInLineList = []
						while(tokens[pos][t] != 'T_LNBRK'):
							tokensInLineList.append(tokens[pos])
							pos+=1
						lineList.append(tokensInLineList)
						pos+=1
					blocks.append((blockName, lineList))
					pos+=1
				else:
					pos+=1
			else:
				pos+=1
					
			# block processed and added
			# return to loop finding blocks		
		# return the blocks
		return blocks
			
	def process_line(self, tokens):
		t = 0
		v = 1

		# Process list of tokens
		if (len(tokens) == 0): return
		# Prepare for looping
		current = 0
		if (tokens[current][t] == 'T_NUM'):	# 0,0
			
			loopIt = tokens[current][v]	# 0,1
			current+=1
			if (tokens[current][t] == 'T_OPENBRAK'): # 1,0
				current+=1
				if (tokens[current][t] == 'T_STR'): # 2,0
					funcName = tokens[current][v]	# 2,0
					current+=1
					func = self.db.getReturnTypeForFunctionName(funcName)
					if (func == None):	# Not a system function
						for i in range(1,int(loopIt)+1):
							if(self.process_block(funcName) == -1): return
					else:
						for i in range(1,int(loopIt)+1):	# convert below to lambdas?
							if (len(func) == 1):
								getattr(self.gc, func[0])()
							if (len(func) == 2):
								if (tokens[current+1][0] == func[1]):
									getattr(self.gc, func[0])(tokens[current+1][1])
							elif (len(func) == 3):
								if (tokens[current+1][0] == func[1] and tokens[current+3][0] == func[2]):
									getattr(self.gc, func[0])(tokens[current+1][1],tokens[current+3][1])
		
		elif (tokens[current][t] == 'T_STR'): # 0,0
			funcName = tokens[current][v]	# 0,1
			current+=1
			func = self.db.getReturnTypeForFunctionName(funcName)
			if (func == None):	# Not a system function
				if(self.process_block(funcName) == -1): 
					return
			else:
				if (len(func) == 1):
					getattr(self.gc, func[0])()
				if (len(func) == 2):
					if (tokens[current+1][0] == func[1]):
						getattr(self.gc, func[0])(tokens[current+1][1])
				elif (len(func) == 3):
					if (tokens[current+1][0] == func[1] and tokens[current+3][0] == func[2]):
						getattr(self.gc, func[0])(tokens[current+1][1],tokens[current+3][1])
				
		return 0
	
	def process_block(self, blockName):
			block = self.db.getLocalBlockByName(blockName)
			if (block == None):
				print "[-] " + blockName + " called, but not found."
				return -1
			else:
				for x in block:
					self.process_line(x)
			
	def process_file(self, fileContents):
		self.db.addBlocks(self.createBlocks(self.tokenize(fileContents)))
		print "[*] Running..."
		# Start executing at block 'main'
		mainBlock = self.db.getLocalBlockByName('main')
		if (mainBlock == None):
			print "[-] No main block found."
			return -1
		else:
			self.startGC()
			for x in mainBlock:
				self.process_line(x)
		return 0
		

	def nextCh(self,string, pos):
		if (pos+1 < len(string)):
			return string[pos+1]
		else:
			return len(string)
								
			
