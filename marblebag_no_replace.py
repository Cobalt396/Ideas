import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

prints = False

x = [1, 2, 3]

width = 0.75

rMarbles = 50
gMarbles = 30
bMarbles = 40

numPicks = (rMarbles + gMarbles + bMarbles) // 2

def addMarbles(rNum, gNum, bNum):
	bag = rNum * ["red"] + gNum * ["green"] + bNum * ["blue"]

	if prints:
		print(bag)
	return bag

def pickMarbles(bag):
	choice = random.randrange(0, len(bag))

	if bag[choice] == "red":
		if prints:
			print("it's red!")
		bag.pop(choice)
		return "red"

	elif bag[choice] == "green":
		if prints:
			print("it's green!")
		bag.pop(choice)
		return "green"

	elif bag[choice] == "blue":
		if prints:
			print("it's blue!")
		bag.pop(choice)
		return "blue"

	else:
		print("error, marble color not found")

def checkPicks(bag):
	redPick = 0
	greenPick = 0
	bluePick = 0

	for i in range(numPicks):
		result = pickMarbles(bag)

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
        ax.annotate('{}%'.format(round(height * 100, 2)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 2),  # 2 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

marbleBag = addMarbles(rMarbles, gMarbles, bMarbles)

if prints:
	print("Bag before picks: ", marbleBag)
	print("Len of bag before picks: ", len(marbleBag))

(rResults, gResults, bResults) = checkPicks(marbleBag)

if prints:
	print("Red results: ", rResults)
	print("Green results: ", gResults)
	print("Blue results: ", bResults)

	print("Bag after picks: ", marbleBag)
	print("Len of bag after picks: ", len(marbleBag))


formatter = FuncFormatter(percents)

valsR = [rResults/numPicks]
valsG = [gResults/numPicks]
valsB = [bResults/numPicks]

rL = "Red: " + str(rResults) # + " Theoretical: " + str(redTheory * 100) + "%"
gL = "Green: "+str(gResults) # + " Theoretical: " + str(greenTheory * 100) + "%"
bL = "Blue: " + str(bResults) #+ " Theoretical: " + str(blueTheory * 100) + "%"

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

ax.legend(loc = 'lower left', fancybox=True, shadow=True, title="Num Picked")

ax.set_ylabel('Percentages')
ax.set_xlabel('Marble Colors')
ax.set_title('Percentages of Colored Marbles Picked from Bag')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()