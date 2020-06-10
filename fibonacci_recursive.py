def fib(n):
	'''function for recursive formula of fib sequence'''
	if n <= 2:
		#the first two terms should both be 1
		return 1
	else:
		#if n is not the first two terms then find the value of the nth term
		return fib(n - 1) + fib(n - 2)

#index of the final term outputed
y = 1000

#loops using the recursive fn above until reaching nth term
for x in range(y + 1):
	print(fib(x))