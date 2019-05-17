# -*- coding: utf-8 -*-
from gameLogic import *

print("Choosing a movies' name.")

nextGame = False
globalPoints = 0
guessedMovies = 0

game = getMovieNames()
game.setUp()

while (nextGame == False):
	print("Round {}, points: {}.".format(guessedMovies, globalPoints))
	name, year, clues = game.downloadNames()
	codeName = GameLogic(name, globalPoints)

	try:
		print("Clues.\nReleased date: {}.\nDescription: {}".format(year, clues))
	except UnicodeEncodeError:
		print("Clues.\nReleased date: {}.\nDescription: Not available.".format(year))

	for i in codeName.hideNameArray():
		print i,

	tries = len(name) + len(name)/2
	ending = False

	while tries > 0 and ending == False:

		print("\nYou have {} tries left.\nPoints: {}".format(tries, codeName.points))
		playerLetter = raw_input("\nWrite a letter:\n")

		if len(playerLetter) == 1:
		
			gamePlay, tried = codeName.checkGuessedLetters(playerLetter)

			for i in gamePlay:
				print i,
			print("\n")

			ending = codeName.checkWin()
			tries -= tried

		else:
			print("Just one letter.")
			
	if ending == True:
		print "You won this round."
		guessedMovies += 1
		globalPoints += codeName.points
	else:
		print "You lost. The name was {}".format(name)
		nextGame = True

playerName = raw_input("\nWrite your name: ")
codeName.saveNewRecord(playerName)