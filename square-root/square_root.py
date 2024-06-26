def square_root(number):
    # n^2 is the sum of the first n odd numbers squared
    root = 0

    while number > 0:
        root += 1
        number -= 2 * root - 1

    return root