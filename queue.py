import random

class myQueue:
	'''A queue'''

	def __init__(self):
		self.queue = []

	def look(self):
		return self.queue[0]

	def remove(self):
		return self.queue.pop(0)

	def add(self, value):
		self.queue.append(value)

thisQueue = myQueue()

for i in range(15):
	thisQueue.add(random.randrange(1, 100))

for i in range(3):
	print("Queue: ", thisQueue.queue)

	print("Top of the Queue: ", thisQueue.look())

	print("Removed ", thisQueue.remove())

	print("Updated Queue: ", thisQueue.queue)