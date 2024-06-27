def is_valid(isbn):
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    if 'X' in isbn and not isbn.endswith('X'):
        return False

    if not isbn.replace('X', '').isnumeric():
        return False
    
    digits_sum = sum(
        (10 - index) * (int(digit) if digit != 'X' else 10)
        for index, digit in enumerate(isbn)
    )

    return digits_sum % 11 == 0
