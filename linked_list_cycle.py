class node:
	'''Element of the linked list'''

	def __init__(self, value, nextV = -1):
		self.nodeValue = value
		self.nodeNext = nextV

	def isEnd(self):
		if isinstance(self.nodeNext, int):
			return True

		return False

class myLinkedList:
	'''A linked list'''

	def __init__(self, head):
		self.listHead = head

	def addAtEnd(self, newV):
		newNode = node(newV)

		if self.listHead.isEnd():
			self.listHead.nodeNext = newNode
			return

		currentNode = self.listHead

		while not currentNode.isEnd():
			currentNode = currentNode.nodeNext

		currentNode.nodeNext = newNode

	def addAtBeginning(self, newV):
		newNode = node(newV, self.listHead)

		self.listHead = newNode

	def deleteHead(self):
		self.listHead = self.listHead.nodeNext

	def deleteNode(self, targetV):
		if self.listHead.isEnd(): 
			return

		currentNode = self.listHead

		while not currentNode.nodeNext.isEnd():
			if currentNode.nodeNext.nodeValue == targetV:
				currentNode.nodeNext = currentNode.nodeNext.nodeNext
				return

			currentNode = currentNode.nodeNext


	def printLL(self):
		currentNode = self.listHead

		print("---Start---")

		while not currentNode.isEnd():
			print(currentNode.nodeValue)
			currentNode = currentNode.nodeNext

		print(currentNode.nodeValue)
		print("---End---")

	def tortoiseAndHare(self):
		tortoise = self.listHead
		hare = self.listHead.nodeNext

		print("Hare at end?: ", hare.isEnd())

		while not hare.isEnd():
			print("Hare: ", hare.nodeValue)
			print("Tortoise: ", tortoise.nodeValue)
			print("Hare at end?: ", hare.isEnd())

			if hare.isEnd() or hare.nodeNext.isEnd():
				print("Hare: ", hare.nodeValue)
				print("Tortoise: ", tortoise.nodeValue)
				print("The list has no cycle")
				return

			if tortoise == hare:
				print("Hare: ", hare.nodeValue)
				print("Tortoise: ", tortoise.nodeValue)
				print("The list has a cycle")
				return

			tortoise = tortoise.nodeNext
			hare = hare.nodeNext.nodeNext

myLL = myLinkedList(node(1))

myLL.addAtEnd(2)
myLL.addAtEnd(3)
myLL.addAtEnd(4)
myLL.addAtEnd(5)
myLL.addAtEnd(6)
myLL.addAtEnd(7)
myLL.addAtEnd(8)
myLL.addAtEnd(9)

myLL.listHead.nodeNext.nodeNext.nodeNext.nodeNext.nodeNext.nodeNext.nodeNext.nodeNext = myLL.listHead.nodeNext.nodeNext.nodeNext

myLL.tortoiseAndHare()
# myLL.printLL()