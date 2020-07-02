import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

prints = False

numPicks = 500

x = [1, 2, 3]

width = 0.75

redBalls = 3
greenBalls = 2
blueBalls = 4

loops = 1000

rRes = []
gRes = []
bRes = []

def addMarbles(rNum, gNum, bNum):
	bag = rNum * ["red"] + gNum * ["green"] + bNum * ["blue"]

	if prints:
		print(bag)
	return bag

def pickMarble(bag):
	choice = random.randrange(0, len(bag))

	if bag[choice] == "red":
		if prints:
			print("it's red!")
		return "red"

	elif bag[choice] == "green":
		if prints:
			print("it's green!")
		return "green"

	elif bag[choice] == "blue":
		if prints:
			print("it's blue!")
		return "blue"

	else:
		print("error, marble color not found")

def checkPicks(bag):
	redPick = 0
	greenPick = 0
	bluePick = 0

	for i in range(numPicks):
		result = pickMarble(bag)

		if result == "red":
			redPick += 1
		elif result == "green":
			greenPick += 1
		elif result == "blue":
			bluePick += 1

	if prints:
		print("red was picked ", redPick, " times")
		print("green was picked ", greenPick, " times")
		print("blue was picked ", bluePick, " times")

	return(redPick, greenPick, bluePick)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(round(height * 100, 3)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 2),  # 2 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

marbleBag = addMarbles(redBalls, greenBalls, blueBalls)
if prints:
	print(marbleBag)
# pickMarble(marbleBags)

for i in range(loops):
	(redResults, greenResults, blueResults) = checkPicks(marbleBag)

	rRes.append(redResults)
	gRes.append(greenResults)
	bRes.append(blueResults)

rPer = [ind / numPicks for ind in rRes]
gPer = [ind / numPicks for ind in gRes]
bPer = [ind / numPicks for ind in bRes]

redTheory = round(redBalls / (redBalls + greenBalls + blueBalls), 2)
greenTheory = round(greenBalls / (redBalls + greenBalls + blueBalls), 2)
blueTheory = round(blueBalls / (redBalls + greenBalls + blueBalls), 2)

if True:
	print(redResults)
	print(greenResults)
	print(blueResults)

	print(redResults/numPicks)
	print(greenResults/numPicks)
	print(blueResults/numPicks)	

	print(np.mean(rRes))
	print(np.mean(gRes))
	print(np.mean(bRes))

rgbLabel = ["Red", "Green", "Blue"]

fig, ax = plt.subplots()

ax.set_ylabel('Percentages')
ax.set_xlabel('Marble Colors')
ax.set_title("Box and Whisker of Multiple Marble Bag Pulls")

ax.boxplot([rPer, gPer, bPer], labels = rgbLabel)

ticks = ax.get_yticks()
ax.set_yticklabels(['{:,.1%}'.format(x) for x in ticks])
# ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 

plt.grid(True)

plt.show()

plt.hist([rRes, gRes, bRes], density = True, bins = 50)

plt.show()