import numpy as np
import random
import pygame

'''
Important part for MVC model

'''
class Controller:
	def __init__(self, model, view):
		self.view = view
		self.model = model

	def play(self):
		print("\033c")
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