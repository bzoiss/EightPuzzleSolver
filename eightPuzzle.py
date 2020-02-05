"""
eightPuzzle.py
ADT for the puzzle
"""

import random

class EPuzzle:
	
	def __init__(self):
		self.puzzle = [[1 for i in range(3)] for j in range(3)]
		self.puzzle = self.genRandomState()

		for i in range(3):
			for j in range(3):
				if (self.puzzle[i][j] == 0):
					self.blankX = j
					self.blankY = i
				# end if
			# end for
		# end for

		self.depth = 0

		self.key = 0
		self.genKey()
	# end init
	
	# prints out the current state
	def printState(self):
		for i in range(3):
			for j in range(3):
				print ("{}".format(self.puzzle[i][j]), end = " ")
			# end for
			print ()
		# end for
	# end getState

	# returns true if this puzzle is the same as the one passed in, otherwise returns false
	def isEqual(self, p):
		for i in range(3):
			for j in range(3):
				if (self.puzzle[i][j] != p[i][j]):
					return False
				# end if
			# end for
		# end for
		return True
	# end isEqual

	# returns a random state of the puzzle
	def genRandomState(self):
		combination = [1, 2, 3, 4, 5, 6, 7, 8, 0]
		# random.shuffle shuffles the elements of the list in a random order
		random.shuffle(combination)
		
		# need a counter to place all elements
		counter = 0
		for i in range(3):
			for j in range(3):
				self.puzzle[i][j] = combination[counter]
				counter += 1
			# end for
		# end for

		return self.puzzle
	# end genRandomState
	
	# returns the number of misplaced tiles in the puzzle
	def numMisplaced(self):
		goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
		counter = 0
		for i in range(3):
			for j in range(3):
				if (self.puzzle[i][j] != goal[i][j]):
					counter += 1
				# end if
			# end for
		# end for
		return counter
	# end numMisplace
	
	# method to place objects in a priority queue
	def __lt__(self, other):
		return (self.numMisplaced() + self.depth) < (other.numMisplaced() + other.depth)
	# end __lt__

	# method to generate a unique key to make identification easier
	def genKey(self):
		key = 0
		count = 1
		for i in range(3):
			for j in range(3):
				key += self.puzzle[i][j]**count
				count += 1
			# end for
		# end for
		self.key = key
	# end genKey
# end EPuzzle
