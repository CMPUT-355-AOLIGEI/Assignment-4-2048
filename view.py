import numpy as np
import random
import pygame



'''
Should implement the pygame part here, never change the model for displaying stuff.
write new codes associate with pygame to get fancy interface.


'''

class View:
	def __init__(self,model):
		self.model = model

	def printBoardEasy(self):
		foregroundColor = ""
		backgroundColor = ""
		board = self.model.getBoard()
		for row in board:
			for col in row:

				print("%d"%col,end=" ")
			print("\n")

	def printScore(self):
		print("current Score is %d"%self.model.getScore())

