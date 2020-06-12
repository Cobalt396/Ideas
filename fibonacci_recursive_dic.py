import time

nums = {}

def fib(n):
	'''function for recursive formula of fib sequence'''
	if n <= 2:
		#the first two terms should both be 1
		return 1
	elif n in nums:
		return nums[n]
	else:
		#if n is not the first two terms then find the value of the nth term
		z = fib(n - 1) + fib(n - 2)
		nums[n] = z

		return z

#index of the final term outputed
y = 1000

start_time = time.time()

#loops using the recursive fn above until reaching nth term
for x in range(y + 1):
	print(fib(x))

print("--- %s seconds ---" % (time.time() - start_time))