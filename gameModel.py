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
		return np.where(self.board==Model.emptyCellChar)

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
		# get all the available based on current game table.
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
		self.board[index[0],index[1]]=newValue

	def move(self,direction):
		# direction == a means all cells move left
		# d: right
		# w: up
		# s: down
		resultboard,baseboard = None, None
		rows, cols = None, None
		if direction == "w":
			baseboard = self.board.T

		elif direction == "a":
			baseboard = self.board

		elif direction == "s":
			baseboard = np.flip(self.board.T,axis=1)

		elif direction == "d":
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
		
		for row_index in range(board.shape[0]):
			tempRowList = copy.deepcopy(board[row_index])
			# get all values that's not zero in a row
			tempRowList = tempRowList[tempRowList !=0] 
			if len(tempRowList) != 0:
				combine_index=0
				if len(tempRowList) == 1:
					tempboard[row_index,combine_index] = tempRowList[0]
				else:

					for cell_index in range(len(tempRowList)): # TODO: switch to while loop
						if tempRowList[cell_index] !=0:
							if cell_index == len(tempRowList)-1:
								tempboard[row_index,combine_index] = tempRowList[cell_index]

							elif tempRowList[cell_index] == tempRowList[cell_index+1]:
						
								newValue = tempRowList[cell_index]<<1
								self.setScore(self.getScore()+newValue)   # score = score + newValue
								tempboard[row_index,combine_index] = newValue
								tempRowList[cell_index+1] = 0	
							else:
								tempboard[row_index,combine_index] = tempRowList[cell_index]
							tempRowList[cell_index] = 0
							combine_index+=1
					



