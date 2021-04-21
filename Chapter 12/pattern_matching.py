def search(pattern, txt_string):
    pattern_length = len(pattern)
    string_length = len(txt_string)

    # A loop to slide pattern[] one by one
    for i in range(string_length - pattern_length + 1):
        j = 0

        # For current index i, check for pattern match
        for j in range(0, pattern_length):
            if txt_string[i + j] != pattern[j]:
                break

        if j == pattern_length - 1:
            print("Match found at index ", i)


if __name__ == "__main__":
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)
