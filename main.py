"""
main.py
The main driver of the program
"""

from eightPuzzle import EPuzzle

import queue, copy

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def main():
	# 3 puzzles
	for i in range(3):
		p = EPuzzle()
		print("Current state:")
		p.printState()

		print("BFS: {}".format(BFS(p)))
		print("A*: {}".format(aStar(p)))
		print()
	# end for

# end main

def BFS(p):
	# standard library queue
	fringe = queue.Queue()
	closed = []

	fringe.put(p)
	
	keepGoing = True
	while (keepGoing):
		if (fringe.empty()):
			return False
		# end if
		node = copy.deepcopy(fringe.get())
		
		closed.append(node.key)
		if (node.isEqual(goal)):
			return True
		# end if
		children = genExpansion(node, closed)
		# add each element of children to the queue
		for i in range(len(children)):
			fringe.put(children[i])
		# end for
	# end while
# end BFS

def aStar(p):
	# standard library priority queue
	fringe = queue.PriorityQueue()
	closed = []

	fringe.put(p)

	keepGoing = True
	while (keepGoing):
		if (fringe.empty()):
			return False
		# end if
		node = copy.deepcopy(fringe.get())

		closed.append(node.key)
		if (node.isEqual(goal)):
			return True
		# end if
		children = genExpansion(node, closed)
		# add each child to the priority queue f(n) = depth + number of misplaced tiles
		for i in range(len(children)):
			fringe.put(children[i])
		# end for
	# end while
# end AStar

def genExpansion(node, closed):
	children = []
	
	curX = node.blankX
	curY = node.blankY
	
	# swap right
	if not(curX + 1 > 2):
		newNode = copy.deepcopy(node)

		temp = newNode.puzzle[curY][curX]
		newNode.puzzle[curY][curX] = newNode.puzzle[curY][curX + 1]
		newNode.puzzle[curY][curX + 1] = temp
		
		newNode.blankX = curX + 1
		newNode.genKey()
		if not(newNode.key in closed):
			children.append(newNode)
		# end if
	# end if
	# swap left
	if not(curX - 1 < 0):
		newNode = copy.deepcopy(node)

		temp = newNode.puzzle[curY][curX]
		newNode.puzzle[curY][curX] = newNode.puzzle[curY][curX - 1]
		newNode.puzzle[curY][curX - 1] = temp
		
		newNode.blankX = curX - 1
		newNode.genKey()
		if not(newNode.key in closed):
			children.append(newNode)
		# end if
	# end if
	# swap up
	if not(curY + 1 > 2):
		newNode = copy.deepcopy(node)

		temp = newNode.puzzle[curY][curX]
		newNode.puzzle[curY][curX] = newNode.puzzle[curY + 1][curX]
		newNode.puzzle[curY + 1][curX] = temp
		
		newNode.blankY = curY + 1
		newNode.genKey()
		if not(newNode.key in closed):
			children.append(newNode)
		# end if
	# end if
	# swap down
	if not(curY - 1 < 0):
		newNode = copy.deepcopy(node)

		temp = newNode.puzzle[curY][curX]
		newNode.puzzle[curY][curX] = newNode.puzzle[curY - 1][curX]
		newNode.puzzle[curY - 1][curX] = temp
		
		newNode.blankY = curY - 1
		newNode.genKey()
		if not(newNode.key in closed):
			children.append(newNode)
		# end if
	# end if

	# add one to the depth of all
	for i in children:
		i.depth += 1
	return children
# end genExpansion

# starts the program
if (__name__ == "__main__"):
	main()
# end if
