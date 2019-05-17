# -*- coding: utf-8 -*-
import random
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class getMovieNames():
	"""docstring for getMovieNames"""
	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		self.driver = webdriver.Chrome(chrome_options=options)

	def downloadNames(self):
		'''Selects a movie''' 
		
		self.driver.get("https://www.imdb.com/list/ls005578473/")
		getTitles = self.driver.find_elements_by_tag_name("h3")
		getClues = self.driver.find_elements_by_xpath("//div[@class='lister-item-content']/p[@class='']")

		titles = [x.text for x in getTitles]
		clue = [x.text for x in getClues]
		
		selection = random.randint(0, 101)
		title = titles[selection].split()
		title.pop(0)
		year = title.pop(-1)
		title = " ".join(title)
		
		return title, year, clue[selection]

	def getName(self):
		""" Selects a name in the file"""
		try:
			f = open("games", "r")
			
			f1 = f.readlines()
			listNames = [line.replace("\n", "").lower() for line in f1]
			f.close()

			selection = random.randint(0, len(listNames) - 1)
			name = listNames[selection]
			return name

		except IOError:
			print("No file called 'games'.")
			return False


class GameLogic():
	"""Game logic"""

	def __init__(self, name, points = 0, hiddenName = ""):
		self.name = name
		self.points = points
		self.hiddenName = hiddenName

	def hideNameArray(self):
		""" Makes an array with * from the name """
		self.hiddenName = ["*" if letter.isalpha() else letter for letter in self.name ]
		return self.hiddenName

	def checkGuessedLetters(self, givenLetter):
		""" Add the guessed letters """		
		tries = 0
		if givenLetter not in self.hiddenName:
			for position, letter in enumerate(self.name):
				
				if letter.lower() == givenLetter.lower():
					self.hiddenName[position] = givenLetter
					self.points += 2
			if self.name.find(givenLetter) == -1:
				self.points -= 1
				tries = 1
		return self.hiddenName, tries

	def checkWin(self):
		""" Checks if all letters have been guessed """

		if '*' in self.hiddenName:
			return False
		
		return True
		
	def saveNewRecord(self, playerName):
		""" Saves the winner's name in a file"""
		f = open("Records", "a")
		
		f.write("Name: {}, points: {}, date: {}.\n".format(playerName, self.points, datetime.datetime.now()))
		f.close()

		return self.name
