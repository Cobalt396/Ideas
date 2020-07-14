import random

class myStack:
	'''A stack'''

	def __init__(self):
		self.stack = []

	def look(self):
		return self.stack[len(self.stack) - 1]

	def remove(self):
		return self.stack.pop(len(self.stack) - 1)

	def add(self, value):
		self.stack.append(value)

thisStack = myStack()

for i in range(15):
	thisStack.add(random.randrange(1, 100))

for i in range(3):
	print("Stack: ", thisStack.stack)

	print("Top of the stack: ", thisStack.look())

	print("Removed ", thisStack.remove())

	print("Updated stack: ", thisStack.stack)