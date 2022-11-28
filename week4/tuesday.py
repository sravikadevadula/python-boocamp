# 1
def func(n):
		for i in range(n):
				for j in range(n):
						if j < I:
								break
#time complexity = O(n2)
# 2
def func(L):
		for v in L:
				# helper func time complexity is O(n)
				helper_func(v)
# time complexity = O(n2)
# 3
def func(n):
		j = n
		while j > 0:
				j = j // 2
		while j<n:
				j = j + 3
				n = n - 5
		return j
# time complexity = O(log(n))
# 4
def func(n):
		total = 0
		while n > 5:
				n = n // 2
				# Remember the time complexity of the sum and range methods
				total += sum(range(n))
		return total
# time complexity = O(log n)
# 5
def func(n):
	for i in range(2,n):
			if n % i == 0:
					return True
			if i > n/i:
					return False
# time complexity = O(n)
# 6
def func(n):
		for i in range(n):
				for j in range(i):
						if j * j > I:
								break
# time complexity = O(n2)
# 7
def func(n):
		k=0
		for i in range(n//2, n):
				j=1
		    while (j <= n):
		        k += 1
						j *= 2
		return k
# time complexity = 0(nlog(n))
# 8
def helper_func(x):
		for i in range(x):
				print(i)
		return x

def func(n):
		if n == 2:
				return 0
		else:
				return helper_func(n - 1) + helper_func(n - 2)
# time complexity = O(n)
# 9
def helper_func(n):
		for i in range(n**2):
		        print(i)
def func(n):
		for i in range(n**2):
				print(helper_func(100))
		return 0
# time complexity = O(n2)