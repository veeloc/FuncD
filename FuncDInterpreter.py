#import modules
import os, sys, time
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
		
	def tokenize(self, string):
		if (len(sys.argv) > 1):
			if (sys.argv[1] == '-t'):
				t0 = time.time()

		tokens = []
		# Loop over every character and begin to tokenize
		pos = 0
		
		while (pos < len(string)):
			
			x = string[pos]
			t = 'T_NULL'
			
			# Test for numbers
			if x == '0' or x == '1' or x == '2'\
			or x == '3' or x == '4' or x == '5'\
			or x == '6' or x == '7' or x == '8' or x == '9':
				t = 'T_NUM'
				next = self.nextCh(string, pos)	
				if next == '0' or next == '1' or next == '2'\
				or next == '3' or next == '4' or next == '5'\
				or next == '6' or next == '7' or next == '8' or next == '9':
					pos += 1
					temp = string[pos]
					while temp == '0' or temp == '1' or temp == '2'\
						or temp == '3' or temp == '4' or temp == '5'\
						or temp == '6' or temp == '7' or temp == '8' or temp == '9' and pos < len(string):
						x += temp
						pos += 1
						if (pos < len(string)):
							temp = string[pos]
						else:
							break
					pos -= 1
						
			# Test for special characters
			elif x == '/':
				if (self.nextCh(string, pos) == '/'):
					t = 'T_COMMENT'
					pos += 1
					temp = string[pos]
					while temp != '\n':
						temp = string[pos]
						pos += 1
						
				else:
					t = 'T_UNKNOWN'
			elif x == '[':
				t = 'T_OPENBRAK'
			elif x == ']':
				t = 'T_CLOSEBRAK'
			elif x == '(':
				t = 'T_OPENPAR'
			elif x == ')':
				t = 'T_CLOSEPAR'
			elif x == ';':
				t = 'T_SEMIC'
			elif x == ',':
				t = 'T_COM'
			elif x == ':':
				t = 'T_COL'
			elif x == '>':
				t = 'T_V'
				if (self.nextCh(string, pos) == '>'):
					t = 'T_VV'
					pos += 1
					temp = string[pos]
				
			elif x == 'a' or x == 'b' or x == 'c'\
			 or x == 'd' or x == 'e' or x == 'f'\
			 or x == 'g' or x == 'h' or x == 'i'\
			 or x == 'j' or x == 'k' or x == 'l'\
			 or x == 'm' or x == 'n' or x == 'o'\
			 or x == 'p' or x == 'q' or x == 'r'\
			 or x == 's' or x == 't' or x == 'u'\
			 or x == 'v' or x == 'w' or x == 'x'\
			 or x == 'y' or x == 'z'\
			 or x == 'A' or x == 'B' or x == 'C'\
			 or x == 'D' or x == 'E' or x == 'F'\
			 or x == 'G' or x == 'H' or x == 'I'\
			 or x == 'J' or x == 'K' or x == 'L'\
			 or x == 'M' or x == 'N' or x == 'O'\
			 or x == 'P' or x == 'Q' or x == 'R'\
			 or x == 'S' or x == 'T' or x == 'U'\
			 or x == 'V' or x == 'W' or x == 'X'\
			 or x == 'Y' or x == 'Z':
				
				t = 'T_STR'
				next = self.nextCh(string, pos)
				if next == 'a' or next == 'b' or next == 'c'\
				 or next == 'd' or next == 'e' or next == 'f'\
				 or next == 'g' or next == 'h' or next == 'i'\
				 or next == 'j' or next == 'k' or next == 'l'\
				 or next == 'm' or next == 'n' or next == 'o'\
				 or next == 'p' or next == 'q' or next == 'r'\
				 or next == 's' or next == 't' or next == 'u'\
				 or next == 'v' or next == 'w' or next == 'x'\
				 or next == 'y' or next == 'z'\
				 or next == 'A' or next == 'B' or next == 'C'\
				 or next == 'D' or next == 'E' or next == 'F'\
				 or next == 'G' or next == 'H' or next == 'I'\
				 or next == 'J' or next == 'K' or next == 'L'\
				 or next == 'M' or next == 'N' or next == 'O'\
				 or next == 'P' or next == 'Q' or next == 'R'\
				 or next == 'S' or next == 'T' or next == 'U'\
				 or next == 'V' or next == 'W' or next == 't'\
				 or next == 'Y' or next == 'Z':
					pos += 1
					temp = string[pos]
					while temp == 'a' or temp == 'b' or temp == 'c'\
					or temp == 'd' or temp == 'e' or temp == 'f'\
					or temp == 'g' or temp == 'h' or temp == 'i'\
					or temp == 'j' or temp == 'k' or temp == 'l'\
					or temp == 'm' or temp == 'n' or temp == 'o'\
					or temp == 'p' or temp == 'q' or temp == 'r'\
					or temp == 's' or temp == 't' or temp == 'u'\
					or temp == 'v' or temp == 'w' or temp == 'x'\
					or temp == 'y' or temp == 'z'\
					or temp == 'A' or temp == 'B' or temp == 'C'\
					or temp == 'D' or temp == 'E' or temp == 'F'\
					or temp == 'G' or temp == 'H' or temp == 'I'\
					or temp == 'J' or temp == 'K' or temp == 'L'\
					or temp == 'M' or temp == 'N' or temp == 'O'\
					or temp == 'P' or temp == 'Q' or temp == 'R'\
					or temp == 'S' or temp == 'T' or temp == 'U'\
					or temp == 'V' or temp == 'W' or temp == 't'\
					or temp == 'Y' or temp == 'Z' and pos<len(string):
						x += temp
						pos += 1
						if (pos < len(string)):
							temp = string[pos]
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
								
			