# run a simulation of drawing a 7-card hand from a standard 52-card deck.
# approximate the probability of drawing three or four cards of the same value, e.g. 4H, 4C, 4D.
# because i was arguing with dovid and naomi about their rules for go fish (where you have to reshuffle the deck if someone gets dealt a triple).

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


def runsimulation4(numtrials):
	'''
	take in integer numtrials, the number of numtrials to run
	draw a 7-card hand and check for quadruples, and do that numtrials times
	return the fraction of trials that contain quadruples
	'''
	truecount = 0.
	for i in range(0, numtrials):
		if hasquadruple(drawhand()):
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


def hasquadruple(hand):
	'''
	takes in list hand
	return True if hand contains a triple (3 cards of the same value)
	return False otherwise
	'''
	valuelist = countvalues(hand)
	if (4 in valuelist):
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
	'''
	card = card % 52
	valuelist = range(2,11) + ["J", "Q", "K", "A"]
	value = str(valuelist[card / 4])
	suitlist = ["S", "C", "H", "D"]
	suit = suitlist[card % 4]
	return value + suit


def samevalue(card1, card2):
	'''
	takes in two integers from 0 to 51 corresponding to cards
	return True if these cards should be interpreted as having the same value
	'''
	# NOTE: not used anywhere else in the code
	if (abs(card1 - card2) < 4) and (card2/4 == card1/4):
		return True
	else:
		return False