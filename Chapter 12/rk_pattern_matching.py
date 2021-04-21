chars = 256  # Number of characters in the input alphabet


def search(txt_pattern, txt_string, prime):
	patt_length = len(txt_pattern)
	str_length = len(txt_string)
	i = 0
	j = 0
	patt_hash = 0  # hash value for pattern
	str_hash = 0  # hash value for txt
	h = 1  	# h = pow(d, M-1) % q

	for i in range(patt_length - 1):
		h = (h * chars) % prime

	# Calculate the hash values of pattern and first window of text
	for i in range(patt_length):
		patt_hash = (chars * patt_hash + ord(txt_pattern[i])) % prime
		str_hash = (chars * str_hash + ord(txt_string[i])) % prime

	for i in range(str_length-patt_length+1):  # Slide the pattern over text one by one
		if patt_hash == str_hash:  # Compare hash values
			for j in range(patt_length):  # Check for characters one by one
				if txt_string[i + j] != txt_pattern[j]:
					break

			j += 1
			if j == patt_length:  # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
				print("Pattern found at index " + str(i))

		if i < str_length - patt_length:  # Calculate hash value for next window of text
			str_hash = (chars * (str_hash - ord(txt_string[i]) * h) + ord(txt_string[i + patt_length])) % prime
			if str_hash < 0:  # If text_hash < 0, convert to positive
				str_hash = str_hash + prime


if __name__ == "__main__":
	txt = "GEEKING FOR GEEKS"
	pat = "GEEK"
	q = 101  # A prime number
	search(pat, txt, q)
