def lis_count(list_in, list_length):
	maximum = 1  # Max LIS length

	if list_length == 1:  # Base result
		return 1

	# max_lis is the length of LIS ending with arr[n-1]
	max_lis = 1
	for length in range(1, list_length):
		result = lis_count(list_in, length)
		if list_in[length - 1] < list_in[list_length - 1] and result + 1 > max_lis:
			max_lis = result + 1

		maximum = max(maximum, max_lis)  # Compare max_lis with overall maximum; update if needed

	return maximum


if __name__ == "__main__":
	input_list = [10, 22, 9, 33, 21, 50, 41, 60, 70, 5, 71]
	list_len = len(input_list)
	print(f"Length of LIS is {lis_count(input_list, list_len)}")
