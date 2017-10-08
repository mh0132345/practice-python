def bad_fibonaci(n):
	if n<=1:
		return n
	else:
		return bad_fibonaci(n-1) + bad_fibonaci(n-2)

def good_fibonaci(n):
	if n<=1:
		return(n, 0)
	else:
		(a,b) = good_fibonaci(n-1)
		return (a+b,a)

def main():
	# bad_fibonaci(8)
	fibo = good_fibonaci(99)
	print(fibo[0])

if __name__ == '__main__':
	main()