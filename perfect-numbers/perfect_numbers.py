from math import isqrt


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = []

    end = isqrt(number) + 1

    for div in range(1, end):
        if number % div == 0:
            result = number // div

            if result == div:
                divisors.append(div)
            else:
                divisors.append(div)
                divisors.append(result)

    aliquot_sum = sum(divisors) - number

    if aliquot_sum > number:
        return 'abundant'
    elif aliquot_sum < number:
        return 'deficient'

    return 'perfect'
