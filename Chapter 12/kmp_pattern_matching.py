def kmp_search(txt_pattern, txt_string):
	pattern_length = len(txt_pattern)
	string_length = len(txt_string)

	# create lps[] that will hold the longest prefix suffix values for pattern
	lps = [0] * pattern_length
	j = 0  # index for pattern[]

	# Preprocess the pattern (calculate lps[] array)
	compute_lps_array(txt_pattern, pattern_length, lps)

	i = 0  # index for txt[]
	while i < string_length:
		if txt_pattern[j] == txt_string[i]:  # Match index values
			i += 1
			j += 1

		if j == pattern_length:
			print(f"Found pattern at index {str(i-j)}")
			j = lps[j-1]

		elif i < string_length and txt_pattern[j] != txt_string[i]:  # mismatch after j matches
			if j != 0:  # Ignore lps[0..lps[j-1]] characters, they will match anyway
				j = lps[j-1]
			else:
				i += 1


def compute_lps_array(txt_pattern, pat_length, lps):
	prev_lps_length = 0  # length of the previous longest prefix suffix

	lps[0]  # lps[0] is always 0
	i = 1

	while i < pat_length:  	# Calculate lps[i] for i = 1 to pattern_length - 1
		if txt_pattern[i] == txt_pattern[prev_lps_length]:
			prev_lps_length += 1
			lps[i] = prev_lps_length
			i += 1
		else:
			if prev_lps_length != 0:
				prev_lps_length = lps[prev_lps_length - 1]
			else:
				lps[i] = 0
				i += 1


if __name__ == "__main__":
	txt = "ABABDABACDABABCABAB"
	pat = "ABABCABAB"
	kmp_search(pat, txt)
