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
		for row in self.model.getBoard():
			for col in row:
				print("%d"%col,end=" ")
			print("\n")

	def printScore(self):
		print("current Score is %d"%self.model.getScore())