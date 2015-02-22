class Markov:
	#INSTRUCTIONS FOR USE
	#First, import and create the markov object (import markov, m = markov.Markov()
	#then, load the dictionary (m.loadDictionary)
	#	the script will look for the dictionary as defined by self.dictionaryFile
	#	if it doesn't exist, it'll create an empty dictionary
	#If you need words in your dictionary, use m.appendDictionary(<infile>)
	#	don't forget to m.saveDictionary() so you don't have to update it every time you load the module
	#then just call m.markovString() to be returned a random string!
	#	m.markovString(#) will change the order-size of the markov bot, 1 being default
	# 	be sure to build your dictionary to match the order-size of the bot you're making
	#	otherwise you might run in to some preformance issues.
	#import sys, random
	dictionaryFile = ''
	dictionary = {}
	inputText = ''
	outputLength = 140
	markovOrder = 2
	
	def __init__(self):
		Markov.dictionaryFile = 'defaultDictionary.pkl'
		Markov.dictionary = {}
		Markov.outputLength = 140
		Markov.inputText = ''
		Markov.markovOrder = 2
		print "import succesful"
		
	def saveDictionary(self):
		import cPickle
		inDict = self.dictionaryFile
		inDict2 = open(inDict, 'wb')
		cPickle.dump(self.dictionary, inDict2)
		inDict2.close()	

	def loadDictionary(self):
		import cPickle
		inDictionary=self.dictionaryFile
		#loads a file defined in inDictionary, and then unpickles it 
		#and returns it as a python dictionary to the Class scope
		try: 
			inDict = open(inDictionary, 'rb')
		except:
			print "Warning: unable to find target .pkl file, creating new file"
			inDict = open(inDictionary, 'w+')
			inDict.close()
			inDict = open(inDictionary, 'rb')
		try:
			#this will fail if we just created a new file
			#no need to raise that exception
			dict = cPickle.load(inDict)
		except:
			raise
			dict = {}
		self.dictionary = dict
		inDict.close()
	
	def appendDictionary(self, inFile):
		dictionary = self.dictionary
		order = self.markovOrder
		f = ''
		
		#try and load the inFile for processing into the dictionary
		try:
			file = open(inFile, 'r')
			f = file.read()
			file.close()
			f = f.split(' ')
			#print "opened that shit up"
		except:
			print "Error: Unable to find/open target file"
			raise
			sys.exit()
		
		#index = 0 OFF FOR NEW TEST
		endIndex = len(f)-1
		#endIndex = 400
		#as long as we haven't reached the end of file list, interate through the items
		print endIndex
		#while index < int(endIndex):
		for index in range(0,endIndex):
			#print "index < endIndex"
			window = f[index:index+order]
			#index = index + 1 OFF FOR NEW TEST

			while len(window) > 2:
				window[0] = window [0] + ' ' + window [1]
				window.pop(1)
			#print window	
			if index+order < endIndex:
				#print "if index+order < len(f)"
				if dictionary.has_key(window[0]):
					if dictionary[window[0]].has_key(window[1]):
						dictionary[window[0]][window[1]] = dictionary[window[0]][window[1]] + 1
						#print "found repeat value"
					else:
						dictionary[window[0]][window[1]] = 1
						#print "created key value: " + str(dictionary[window[0]])
				else:
					dictionary[window[0]] = {window[1]: 1}
				#print "created root value: " + str(dictionary[window[0]])
		print "reached end"
		self.dictionary = dictionary
		
	def nextMarkov(self,inKey):
		import random
		#this function looks for the key given as 'inChar' in the defined dictionary
		#if it can't find the key, it returns a random value from the dictionary
		randLimit = 0
		r = random.random()
		if self.dictionary.has_key(inKey):
			#store the dictionary as a list of touples, so we can iterate through the key pairs
			i = self.dictionary[inKey].items()
					
			#determine the total weight of all values for a given key, 
			#and multiply that by our random number r
			#so we can make sure we properly select one of our items
			for key, value in i:
				randLimit = randLimit + value
			r = r * randLimit
			
			for key, value in i:
				if r < value:
					returnVale = key
					break
				else: 
					r = r - value
		else: 
			#this part should really only be called once, otherwise mistakes were made
			#print "rando cardrissian"
			#print inChar
			listDict = self.dictionary.keys()
			r = int(r * len(listDict))
			returnVale = listDict[r]
		#print randMax
		#print "fuck this"
		
		returnVale = returnVale.splitlines()
		returnVale = ' '.join(returnVale)
		
		return returnVale
	
	def markovString(self, keySizeIn=1):
		outputLimit = int(self.outputLength)
		#The first argument should contain the pickled markov dicitonary as created by appendDictionaryWords.py
		#otherwise, fail and end execution

		#increasing this will change how large a window the bot uses when determining the next value
		#not building the dictionary to match the keySize here will result in state-independant randomness
		#which would be not markovian at all, so make sure to build the dictionary correctly.
		keySize = keySizeIn

		#scoping these variables for use, as well as defining the first character in the list
		index = 0
		outString = ''
		#removed brackets around "Markov.nextMarkov(self, '')"
		#added line outStringSplit = outStringSplit.split(' ')
		outStringSplit = self.nextMarkov('')
		outStringSplit = outStringSplit.split(' ')
		
		
		while len(outString) <= outputLimit:
			key = keySize
			keyWord = []
			#this attempts to build a keylength that matches the defined keySize
			#however, it is still broken. Limit keySize to 1 for now
			while key > 0:
				try:
					keyWord.append(outStringSplit[len(outStringSplit)-key])
				except:
					#print 'except'
					keyWord.append(outStringSplit[len(outStringSplit)-1])
					break
				key = key - 1
			#concacinate the keyWord list, pass it to nextChar()
			keyWordStr = ' '.join(keyWord)
			outStringSplit.append(self.nextMarkov(keyWordStr))
			#and then build the string to check the lenght value against the outputLimit
			outString = ' '.join(outStringSplit)
			index += 1

		#since we had to go beyond the outputLimit to stop producing, pop the value that sent us over the outputLimit
		#and then build the final string for output!		
		outStringSplit.pop()
		outString = ' '.join(outStringSplit)

		return outString