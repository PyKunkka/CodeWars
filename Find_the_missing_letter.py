def find_missing_letter(chars):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0

    if chars[0].islower():
        alphabet = alphabet.lower()
        index_start = alphabet.index(chars[0])
        index_finish = alphabet.index(chars[len(chars) - 1])
        for j in range(index_start, index_finish):
            if chars[i] != alphabet[j]:
                return alphabet[j]
            else:
                i += 1
    else:
        index_start = alphabet.index(chars[0])
        index_finish = alphabet.index(chars[len(chars) - 1])
        for j in range(index_start, index_finish):
            if chars[i] != alphabet[j]:
                return alphabet[j]
            else:
                i += 1