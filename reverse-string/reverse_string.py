def reverse(text):
    text = list(text)

    reversed = []

    while len(text) > 0:
        reversed.append(text.pop())

    return ''.join(reversed)
