def fibonacci(n1, n2):
	'''fn to add two previous terms (n-1 and n-2) and return n'''
	n = n1 + n2

	#prints to check values of our variables and ensure equation was succesful
	# print("solving...")
	# print("n: " + str(n))
	# print("n1: " + str(n1))
	# print("n2: " + str(n2))

	#return n to update the value of the nth (current) term
	return(n)

def update(x1, x2):
	'''fn to update variables n1 and n2 with the 
	previous values n and n1 respectively'''
	(n1, n2) = (x1, x2)

	#more prints to check success of update
	# print("updating...")
	# print("n: " + str(n))
	# print("n1: " + str(n1))
	# print("n2: " + str(n2))

	#return the new values n1 and n2 to allow for finding the next term
	return(n1, n2)

#initial values of the sequence
n1 = 1
n2 = 1

#the index of the final term outputted
y = 1000

#loops through the adding and updating fns until reaching the desired nth term
for x in range(y - 2):
	n = fibonacci(n1, n2)
	(n1, n2) = update(n, n1)
	print(n)