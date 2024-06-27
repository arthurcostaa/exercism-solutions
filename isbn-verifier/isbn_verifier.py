def is_valid(isbn):
    isbn = list(isbn.replace('-', ''))

    if len(isbn) != 10:
        return False

    if isbn[-1] == 'X':
        isbn[-1] = '10'

    if not all(n.isdigit() for n in isbn):
        return False
    
    digits_sum = sum(
        (10 - index) * int(digit)
        for index, digit in enumerate(isbn)
    )

    return digits_sum % 11 == 0
