import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

prints = False

numPicks = 500

x = [1, 2, 3]

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
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

marbleBag = addMarbles(3, 2, 1)
if prints:
	print(marbleBag)
# pickMarble(marbleBags)
(redResults, greenResults, blueResults) = checkPicks(marbleBag)

if True:
	print(redResults)
	print(greenResults)
	print(blueResults)

	print(redResults/numPicks)
	print(greenResults/numPicks)
	print(blueResults/numPicks)	

formatter = FuncFormatter(percents)

vals = [redResults/numPicks, greenResults/numPicks, blueResults/numPicks]

fig, ax = plt.subplots()
rects = ax.bar(x, vals)
plt.xticks(x, ("Red", "Green", "Blue"))
ticks = ax.get_yticks()
# ax.yaxis.set_major_formatter(formatter)
ax.set_yticklabels(['{:,.1%}'.format(x) for x in ticks])

ax.set_ylabel('Percentages')
ax.set_xlabel('Marble Colors')
ax.set_title('Percentages of Colored Marbles Picked from Bag')

autolabel(rects)

plt.show()