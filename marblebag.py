import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

prints = False

numPicks = 500

x = [1, 2, 3]

width = 0.75

redBalls = 3
greenBalls = 2
blueBalls = 4

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

def percents(x, pos):
	return '%1.1fp' % (x * 100)

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
(redResults, greenResults, blueResults) = checkPicks(marbleBag)

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

formatter = FuncFormatter(percents)

valsR = [redResults/numPicks]
valsG = [greenResults/numPicks]
valsB = [blueResults/numPicks]

rL = "Red: " + str(redResults) + " Theoretical: " + str(redTheory * 100) + "%"
gL = "Green: "+str(greenResults)+" Theoretical: " + str(greenTheory * 100) + "%"
bL = "Blue: " + str(blueResults)+" Theoretical: " + str(blueTheory * 100) + "%"

rColor = (0.85, 0, 0, 0.75)
gColor = (0, 0.85, 0, 0.75)
bColor = (0, 0, 0.85, 0.75)

fig, ax = plt.subplots(figsize = (7, 7))
rects1 = ax.bar(x[0], valsR, width, color = rColor, label = rL)
rects2 = ax.bar(x[1], valsG, width, color = gColor, label = gL)
rects3 = ax.bar(x[2], valsB, width, color = bColor, label = bL)
plt.xticks(x, ("Red", "Green", "Blue"))
ticks = ax.get_yticks()
# ax.yaxis.set_major_formatter(formatter)
ax.set_yticklabels(['{:,.1%}'.format(x) for x in ticks])

ax.legend(bbox_to_anchor = (0.51,0.16))

ax.set_ylabel('Percentages')
ax.set_xlabel('Marble Colors')
ax.set_title('Percentages of Colored Marbles Picked from Bag')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()