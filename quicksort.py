# Set prints True for prints with info and leave false to only get solution
prints = False

#Various lists to test the algortithm
myArr = [4, 1, 30, 7, 11, 10, 15, 3, 27, 9]
# myArr = [9, 5, 1, 17, 31, 21, 60, 6]

# myArr = ["I", "really", "dont", "think", "this", "works"]
# myArr = ["crash", "crap", "crepe", "crow"]
# myArr = list("qwertyuiopasdfghjklzxcvbnm")

if prints:
	print("Len of array: " + str(len(myArr)))

print("Starting list: ", myArr)

def choosePivot(myList):
	'''Simply chooses a pivot in the middle of the list'''
	# The pivot is always halfway through the list
	n = len(myList) // 2
	if prints:
		print("index of pivot: " + str(n))
		print("value of pivot: " + str(myList[n]))
	return(myList[n], n)

def swap(myList, index1, index2):
	'''Takes two indices from a list and swaps their posistion'''
	# Saves the values at the indices 
	x = myList[index1]
	y = myList[index2]
	if prints:
		print("value at index 1 pre-swap: " + str(myList[index1]))
		print("value at index 2 pre-swap: " + str(myList[index2]))

	# Swaps the values at the indices
	myList[index1] = y
	myList[index2] = x
	if prints:
		print("value at index 1 post-swap: " + str(myList[index1]))
		print("value at index 2 post-swap: " + str(myList[index2]))

	return myList

def partition(myList, pivotInd):
	'''Splits a list into two, larger or smaller than the pivot'''
	return((myList[0:pivotInd], myList[pivotInd:len(myList) - 1]))

def Qsort(myList):
	'''Main function which takes a list and outputs the sorted list'''
	# Base case: if the list only has 1 or less items it doesn't need sorting
	if len(myList) <= 1:
		return(myList)

	# Selects the pivot
	(p, pI) = choosePivot(myList)
	if prints:
		print("pivot: " + str(p))
		print("pivot index: " + str(pI))

	# Moves the pivot to the end of the list
	swap(myList, pI, len(myList) - 1)
	if prints:
		print("pivot at end!", myList)

	# Variables needed for the sorting process
	leftIndex = 0
	rightIndex = len(myList) - 1

	indL = 0
	indR = 0

	leftReady = False
	rightReady = False

	'''Loops through the list, finding terms to swap and swapping them
	Checks from the right and left until it finds something 
	to swap on each side'''
	while leftIndex <= rightIndex:
		if prints:
			print("-------------")
			print("info: ", leftIndex, rightIndex, indL, indR, \
				leftReady, rightReady)
			print("current list: ", myList)
		if myList[leftIndex] > p:
			# If it finds something on left to swap it saves it until swap
			leftReady = True
			indL = leftIndex
		else:
			# Else it keeps checking from the left
			leftReady = False
			leftIndex += 1

		if myList[rightIndex] < p:
			# If it finds something on right to swap it saves it until swap
			rightReady = True
			indR = rightIndex
		else:
			# Else it keeps checking from the right
			rightReady = False
			rightIndex -= 1

		if leftReady and rightReady:
			# Once there is something to swap on each side, swap them
			if prints:
				print("Swapping Now!")
			swap(myList, indL, indR)

	if prints:
		print("ready for partition: ", leftIndex)
	# After all the swaps possible are made, the list is split
	(x, y) = partition(myList, leftIndex)
	
	if prints:
		print("list 1 ", x)
		print("list 2 ", y)

	# Process repeated recusively until solved
	finalSort = Qsort(x) + [p] + Qsort(y)

	print("Final list: ", finalSort)	

	return finalSort

# Runs the sort on the specified list
Qsort(myArr)