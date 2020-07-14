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

testLL = myLinkedList(node(7))

testLL.addAtEnd(8)
testLL.addAtEnd(9)
testLL.addAtEnd(7)

testLL.printLL()

testLL.addAtBeginning(2)
testLL.addAtBeginning(1)

testLL.printLL()

testLL.deleteHead()

testLL.printLL()

testLL.deleteNode(7)

testLL.printLL()