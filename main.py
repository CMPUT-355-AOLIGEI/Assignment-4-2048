import numpy as np
import random
import pygame
import controller
import gameModel
import view

def main():
	model = gameModel.Model(4,4)
	gameController = controller.Controller(model,view.View(model))
	gameController.play()
main()
