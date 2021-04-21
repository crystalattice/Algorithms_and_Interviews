def lis(array):
	n = len(array)

	lis_array = [1]*n  # Initialize LIS list

	for i in range(1, n):
		for j in range(0, i):
			if array[i] > array[j] and lis_array[i]< lis_array[j] + 1 :
				lis_array[i] = lis_array[j]+1

	maximum = 0  # LIS length

	for i in range(n):
		maximum = max(maximum, lis_array[i])

	return maximum


if __name__ == "__main__":
	arr = [10, 22, 9, 33, 21, 50, 41, 60, 70, 5, 71]
	print(f"Length of LIS is {lis(arr)}")
