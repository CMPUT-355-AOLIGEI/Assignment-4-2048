import numpy as np
import random
import pygame
import controller
import gameModel
import view

def main():
	row,col = 0, 0
	while True:
		size = input("Please input the size of the game(rows+one single space+columns): ")
		if len(size)==3 and '1'<size[0] and '1'<size[2]:
			row = int(size[0])
			col = int(size[2])
			break

	model = gameModel.Model(row,col)
	gameController = controller.Controller(model,view.View(model))
	gameController.play()
main()
