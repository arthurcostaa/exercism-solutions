def is_isogram(string):
    string = string.replace(' ', '').replace('-', '').lower()

    letters = []

    for char in string:
        if char not in letters:
            letters.append(char)
        else:
            return False

    return True
