import random
import math
import matplotlib.pyplot as plt

bunPop = 100

carryCap = 10 * bunPop

foxPop = 3

bunB = 0.5

foxB = 0.4

huntQuota = [2, 3, 4]

huntNeed = 2

successR = 0.8

def findPops(bunnies, foxes, bBirth, fBirth, hQ, hN, sR):
	kills = 0
	foxDeath = 0

	for kill in range(hQ * foxes):
		killChance = random.random()
		# print(killChance)

		sModifier = sR * (10 * ((bunnies  - kills) / carryCap))

		if bunnies > 0:
			if killChance <= sModifier:
				kills += 1

	bunnies = min(max(math.ceil((bunnies * (1 + bBirth)) - kills), 0), carryCap)

	if kills < (hN * foxes):
		foxDeath = (hN * foxes) - kills

	foxes = max(math.ceil((foxes * (1 + fBirth)) - foxDeath), 0)

	return (bunnies, foxes)

def runSim(bPop, fPop, huntQ, huntN):
	runs = 50

	bunList = [bPop]
	foxList = [fPop]

	print("Bunnies: ", bPop)
	print("Foxes: ", fPop)

	for i in range(runs):
		(bPop, fPop) = findPops(bPop, fPop, bunB, foxB, huntQ, huntN, successR)

		print("Bunnies: ", bPop)
		print("Foxes: ", fPop)

		bunList.append(bPop)
		foxList.append(fPop)

	return (bunList, foxList)

def analyze(quotas):
	finals = []

	[finals.append(runSim(bunPop, foxPop, huntQ, huntNeed)) for huntQ in quotas]

	print(finals)

	return finals

final = analyze(huntQuota)

styleM = ["--d", "-.d", ":d"]
style = ["--", "-.", ":"]

gr = ["#ab9999", "#92747b", "#896379"]
ora = ["#fd9465", "#ec7449", "#db442d"]

for (ind, (bRes, fRes)) in enumerate(final):
	labelText = str(ind+1) + " @ hQ " + str(huntQuota[ind])

	plt.plot(bRes, style[ind], label = "Bunny " + labelText, color=gr[ind])
	plt.plot(fRes, style[ind], label = "Fox " + labelText, color=ora[ind])

plt.title("Bunny and Fox Populations Over Time")
plt.ylabel("Populations")
plt.xlabel("Time")

plt.legend(loc = 'best', fancybox=True, shadow=True, title="Animals")

plt.show()