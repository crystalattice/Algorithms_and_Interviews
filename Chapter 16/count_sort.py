def count_sort(arr):
	"""Sort a string"""
	sorting_arr = [0 for i in range(256)]
	count_arr = [0 for i in range(256)]  # Store count of individual characters
	answer_str = ["" for char in arr]  # Store result as string is immutable

	for i in arr:  	# Store count of each character
		count_arr[ord(i)] += 1  # Get Unicode code point for string

	# Change count_arr[i] so it now contains actual position of this character in sorting_arr
	for i in range(256):
		count_arr[i] += count_arr[i-1]

	# Build the Chapter 16 character array
	for i in range(len(arr)):
		sorting_arr[count_arr[ord(arr[i])]-1] = arr[i]
		count_arr[ord(arr[i])] -= 1

	# Copy the Chapter 16 array to arr, so that arr now contains sorted characters
	for i in range(len(arr)):
		answer_str[i] = sorting_arr[i]
	return answer_str

if __name__ == "__main__":
	arr = "thisIsCamelCase"
	ans = count_sort(arr)
	print(f"When sorted, '{arr}' becomes '{''.join(ans)}'")