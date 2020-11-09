import numpy as np
import random
import copy

class Model:
	emptyCellChar = 0
	def __init__(self, rows, cols):
		self.rows, self.cols = rows, cols
		# row by col matrix for board
		self.board = self.boardGeneration(rows,cols)
		# get two random number to get started
		self.randomNumberGeneration(amount=2) 
		self.score = 0

	def boardGeneration(self, rows, cols):
		# create a new board
		return np.zeros((rows, cols),dtype=np.int16)

	def randomNumberGeneration(self, amount=1):
		# case: at the beginning of the game we need to generate two random numbers
		# 2 or 4
		# in general case, every time we move toward one direction, one of the empty space 
		# will generate a 2 or 4 randomly

		# note: We can choose the probabilities of selecting 2 or 4, finish later.
		emptyCells, emptyAmount = self.getEmptyCell()
		if emptyAmount != 0:
			# if there's empty cells in the board
			if amount == 1:
				# general case, 1 random number after each move
				assert emptyAmount >=1,"can not generate random number"
				r,pos = self.createNumber(amount, emptyCells)
				self.setCell(pos[0],r[0]) # set one cell in the board to our new random value

			elif amount >= 2:
				# game start, we have two initial random number on the board
				assert emptyAmount >=2,"can not generate random number"
				r,pos = self.createNumber(amount, emptyCells)
				# now pos1 != pos2
				for i in range(len(r)):
					self.setCell(pos[i],r[i])
		else:
			# no empty cells
			raise ValueError("No empty cells in the table")

	def createNumber(self, amount, emptyCells):
		# generate an amount of random numbers and their locations
		randomNums = []
		randomIndex = []
		for i in range(amount):
			ran = random.choice([2,4])
			pos = random.choice(emptyCells).tolist()
	
			while pos in randomIndex:
				pos = random.choice(emptyCells)
			randomIndex.append(pos)
			randomNums.append(ran)
		return randomNums,randomIndex

	def getEmptyCellAmount(self):
		# return all the cells in the board that's empty
		return np.where(self.board == Model.emptyCellChar)

	def getEmptyCell(self):
		# return the Empty Cells locations in the board
		cells = np.where(self.board==Model.emptyCellChar)
		# we get something like: [[0 0 0 1 1 1 2 2][0 1 2 0 1 2 0 1]]
		stackedCells = np.stack((cells[0].T,cells[1].T),axis=1)
		# now we have something like: 
		'''
			[[0 0]
			 [0 1]
			 [0 2]
			 [1 0]
			 [1 1]
			 [1 2]
			 [2 0]
			 [2 1]]

		'''
		return stackedCells, stackedCells.shape[0]

	def getAvailableMove(self):
		'''
			get all the available based on current game table.

			logic for this method:
			if board contains 0:
				means that w a s d are all legal moves, return them

			else:
				we want to find out whether there's two cells with the same value are neighbour
				in that way we can have legal moves along their direction, for example:
				[[2,32,64],
				 [2,16,128],
				 [4,8,256]]
				 we wish to check whether two of the cells are neighbour and they have the same value
				 in this case two 2s are adjacent, that means we can move either upward or downward.
				 Same as the horizontal way.

				To achieve this, we need:
				1. for all the rows, we get an array without zero, we remove zeros(empty cells) from it,
				for example: [2,0,0,2,4,4] we will get [2,2,4,4], then loop through every adjacent pair of 
				cells, to check whether they have the same value, if so, means move right or left both are legal moves
				Then append "a" and "d" to a list, since we are sure that they are legal moves and will be returned later on.

				2. check almost the same thing for all the columns, extract a no-zero array for each column,
				check the same thing. As long as we have two values that are the same and they are neighbour,
				"w" and "s" will also be legal moves.

				Finally we return the legal moves list.

		'''
		moveList = []
		if 0 in self.board:

			return ["w","a","s","d"]
		else:
			
			for row_index in range(self.board.shape[0]):
				if moveList != []: break
				verticalRemoveZeroArray = self.board[row_index][self.board[row_index] != 0]
				for col_index in range(len(verticalRemoveZeroArray)):
					if verticalRemoveZeroArray[col_index]==verticalRemoveZeroArray[col_index+1]:
						moveList.append("a")
						moveList.append("d")
						break


			for col_index in range(self.board.shape[1]):
				horizontalRemoveZeroArray = self.board[:,col_index][self.board[col_index] != 0]
				for row_index in range(len(horizontalRemoveZeroArray)):
					if horizontalRemoveZeroArray[row_index] == horizontalRemoveZeroArray[row_index+1]:
						moveList.append("w")
						moveList.append("s")
						return moveList
			return moveList

	def setCell(self,index, newValue):
		# index == (row,col)
		# set the cell at that location to the new value
		self.board[index[0],index[1]] = newValue

	def move(self,direction):
		# direction == a means all cells move left
		# d: right
		# w: up
		# s: down


		'''
			better check the comments in combineCells method below first.

			since we know how to "push" all the cells to the left and do necessary additions
			we don't need to write four functions for move w a s d. We just need to change the input board
			a little bit.
			For example:
			to implement move left, we just need to input our original board for combineCells function
			but this doesn't work for move up, right, down, say for move up, 
			we have a board:
			[[0,2,2,4],
			[0,2,0,0],
			[0,0,0,0],
			[0,0,0,0]]
			now we want to move up, we will have :
			[[0,4,2,4],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]]

			To use the combineCells correctly, first, get the transpose of the board:
			[[0,0,0,0],
			[2,2,0,0],
			[2,0,0,0],
			[4,0,0,0]]
			Input this board to combineCells, we will get:
			[[0,0,0,0],
			[4,0,0,0],
			[2,0,0,0],
			[4,0,0,0]]
			Then, in this "move" method later, we take transpose again 
			to transform the result board back to the original board, then the result should be correct.

			Same thing for move down and right, just need to conside using flip function, combine with using transpose.


		'''
		resultboard,baseboard = None, None
		if direction == "w":
			# case when the user choose to move up
			baseboard = self.board.T

		elif direction == "a":
			# case when the user choose to move left
			baseboard = self.board

		elif direction == "s":
			# case when the user choose to move bottom
			baseboard = np.flip(self.board.T,axis=1)

		elif direction == "d":
			# case when the user choose to move right
			baseboard = np.flip(self.board,axis=1)
		
		rows,cols = baseboard.shape[0],baseboard.shape[1] 

		resultboard = np.zeros((rows, cols),dtype=np.int16)
		
		# means something changed during the move, means this move is legal
		self.combineCells(baseboard,resultboard)
		if direction == "w":
			resultboard = resultboard.T

		elif direction == "s":
			resultboard = np.flip(resultboard,axis=1).T 

		elif direction == "d":
			resultboard = np.flip(resultboard,axis=1)
		self.setBoard(resultboard)
		self.randomNumberGeneration(amount=1)


	def getScore(self):
		# return the current game sctore
		return self.score

	def setScore(self, newScore):
		# set the score to a new value
		self.score = newScore

	def setBoard(self, newBoard):
		# set the game board to a new value
		self.board = newBoard

	def getBoard(self):
		# return the game board
		return self.board

	def combineCells(self, board, tempboard):

		'''
			To implement move, we need to do the following thing:
			say we have one row in the board, [0,2,2,4], we know if we move right
			it will be [0, 0, 4, 4], we move left it will be [4,4,0,0]. 
			We start from the move left case:

			1. get another array that removes all 0s from the array [0,2,2,4], we get [2,2,4]
			2. reserve an empty array [0,0,0,0], same size as the original array.
			3. an index that tracks where we are in the above empty array
			4.
			for all cells in the [2,2,4]:
				check whether it's the same as its next neighbour, first iteration, check 2 and 2
				they are the same, so we can add them up and change [0,0,0,0] in step 2 to [2+2=4,0,0,0]
				add the index in step 3 up by 1.
				in case we consider the 2 in [2,2,4] again, set the two 2s to 0, avoid unnecessary loops.
				the last 4 will keep the value and copy to the result array directly, [4,4,0,0]

				loop through all cells in the row

			5. do the above step for all rows, we get the result.

			Note: in this method instead of create 4 different cases for w a s d, we change the input board,
			after the move right calculation we flip or transpose it back, please check this together with method
			"move" above.
			This method only handle the case for move left.


		'''
		
		for row_index in range(board.shape[0]):
			tempRowList = copy.deepcopy(board[row_index])
			# get all values that's not zero in a row
			tempRowList = tempRowList[tempRowList !=0] 
			if len(tempRowList) != 0:
				combine_index=0
				if len(tempRowList) == 1:
					tempboard[row_index,combine_index] = tempRowList[0]
				else:

					for cell_index in range(len(tempRowList)): 
						if tempRowList[cell_index] !=0:
							if cell_index == len(tempRowList)-1:
								# when this is the last non-zero cell in a row, 
								# means it needs to be copied to the new result board
								tempboard[row_index,combine_index] = tempRowList[cell_index]

							elif tempRowList[cell_index] == tempRowList[cell_index+1]:
						
								newValue = tempRowList[cell_index]<<1 # new value = old value * 2
								self.setScore(self.getScore()+newValue)   # score = score + newValue
								tempboard[row_index,combine_index] = newValue
								tempRowList[cell_index+1] = 0	
							else:
								tempboard[row_index,combine_index] = tempRowList[cell_index]
							tempRowList[cell_index] = 0
							combine_index+=1
					



