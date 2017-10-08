def binary_search(data, target, low, high):
	"""Return True if target is found in indicated portion of a Python list sorted.

	The search only considers the portion from data[low] to data[high] inclusive.
	"""
	if low > high:
		return False # interval is empty; no match
	else:
		mid = (low + high) // 2
		if target == data[mid]: # found a match
 			return True
		elif target < data[mid]:
			# recur on the portion left of the middle
			return binary_search(data, target, low, mid - 1)
		else:
		# recur on the portion right of the middle
			return binary_search(data, target, mid + 1, high)

def main():
	nums = [i for i in range(0,100000)]
	check = binary_search(nums, 89756, 0, 100000)
	print(check)

if __name__ == '__main__':
	main()
