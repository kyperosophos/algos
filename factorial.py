def factorial (n):
	lst = range(1, n + 1)
	result = 1
	for i in lst:
		result *= i
	return result