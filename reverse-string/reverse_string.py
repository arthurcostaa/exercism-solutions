def reverse(text):
    text = list(text)
    middle = len(text) // 2

    for i in range(middle):
        temp = text[i]

        text[i] = text[-1 * (i + 1)]
        text[-1 * (i + 1)] = temp

    return ''.join(text)
