import numpy as np
import random
import pygame

class Controller:
	def __init__(self, model, view):
		self.view = view
		self.model = model

	def play(self):
		while True:
			self.view.printBoardEasy()
			self.view.printScore()
			availableMoves = self.model.getAvailableMove()
			print("available moves",availableMoves)
			if availableMoves == []:
				print("Game Over")
				self.view.printScore()
				return
			action = input("your action:")
			# one in w a s d 
			if action in availableMoves:
				self.model.move(action)
			print("\033c")
		
			


