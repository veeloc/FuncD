import os, sys

#define parse function for raw input
def parse(string):
	if (string == "q" or string == "quit"):
		sys.exit(0)
	elif(string == 'help'):
		print "help!"
	elif(string == ''): return
	elif(string == 'start'): 
		if (fdi.gcStarted == False): fdi.startGC()
	else:
		if (fdi.gcStarted == False): fdi.startGC()
		
		result = fdi.process_line(fdi.tokenize(string))
		if(result != 0):
			if (result == -1):
				print "[-] Bad option."
		

if (len(sys.argv) > 1):
	if (sys.argv[1] == '-i'):
		#initialize FDI
		from FuncDInterpreter import *
		fdi = funcdinterpreter()
		# start FDI main runloop
		while True:
			# get input
			inputString = raw_input(">> ")
			# parse input
			parse(inputString)
		
# print start messages:
print "[*] Welcome to FuncD"

optionString = raw_input("[+] Enter Input Option: ")
if (optionString == "help"):
	print "help"
elif (optionString == "FDI" or optionString == "fdi"):
	#initialize FDI
	from FuncDInterpreter import *
	fdi = funcdinterpreter()
	# start FDI main runloop
	while True:
		# get input
		inputString = raw_input(">> ")
		# parse input
		parse(inputString)

elif (optionString.find("load") == 0):
	# Command to load the file into FuncD
	filePath = optionString[5:]
	if (filePath[-2:] == "fd"):
		f = open(filePath, 'r')
		if (f == ""):
			print "[-] File is blank."
		else:
			# Valid file found.					
			print "[*] Reading file..."
			#initialize FDI
			from FuncDInterpreter import *
			fdi = funcdinterpreter()
			# Load the file
			if fdi.process_file(f.read()) != -1:
				print "[+] FDI:"
				# Ask for input
				while True:
					# get input
					inputString = raw_input(">> ")
					# parse input
					parse(inputString)
	else:
		print "Invalid file extension: " + filePath[-2:]


