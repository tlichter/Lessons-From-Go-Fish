# see http://wp.me/p7Xt00-2X5 for the story that motivated this code.
# pardon the sloppiness - this was written over the course of one plane ride.
# run a simulation of drawing a 7-card hand from a standard 52-card deck.
# approximate the probability of drawing three or four cards of the same value, e.g. 4H, 4C, 4D.

import random

def runsimulation(numtrials):
	'''
	take in integer numtrials, the number of numtrials to run
	draw a 7-card hand and check for triples, and do that numtrials times
	return the fraction of trials that contain triples
	'''
	truecount = 0.
	for i in range(0, numtrials):
		if hastriple(drawhand()):
			truecount += 1
	return truecount / numtrials


def drawhand():
	'''
	picks seven digits from 0 - 51 without replacement, 
	corresponding to drawing cards from a 52-card deck. 
	return a list of 7 digits hand.
	'''
	decklist = range(0,52)
	hand = []
	for i in range (0,7):
		card = random.choice(decklist)
		hand.append(card)
		decklist.remove(card)
	return hand


def hastriple(hand):
	'''
	takes in list hand
	return True if hand contains a triple (3 cards of the same value)
	return False otherwise
	'''
	valuelist = countvalues(hand)
	if (3 in valuelist) or (4 in valuelist):
		return True
	else:
		return False


def countvalues(hand):
	'''
	returns a list of 13 numbers, corresponding to the number of cards valued 2, 3, ..., J, Q, K, A in the hand.
	'''
	cardvalues = [0 for i in range(0,13)]
	for h in hand:
		cardvalues[h/4] += 1
	return cardvalues


def printhand(hand):
	'''
	converts list of numbers hand into card values.
	prints the hand.
	this is for checking if drawhand() is working properly.
	'''
	handstring = ""
	for h in hand:
		handstring += cardtostring(h) + " "
	print handstring


def cardtostring(card):
	'''
	takes in an integer card.
	return the card that corresponds to that number (mod 52).
	0, 1, 2, 3, 4, 5, ..., 51 go to 2S, 2C, 2H, 2D, 3S, 3C, ..., AD.
	helper for printhand().
	'''
	card = card % 52
	valuelist = range(2,11) + ["J", "Q", "K", "A"] # 2, 3, 4, ..., Jack, Queen, King, Ace
	value = str(valuelist[card / 4])
	suitlist = ["S", "C", "H", "D"] # spades, clubs, hearts, diamonds
	suit = suitlist[card % 4]
	return value + suit
