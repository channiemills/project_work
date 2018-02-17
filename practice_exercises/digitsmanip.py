def digitsmanip(number):
    """
    Calculates product of the digits in the provided integer, excluding zeroes
    :param number: Positive integer
    :return: Product of digits in number
    """
    string = str(number)
    answer = 1
    for i in range(len(string)):
        if int(string[i]):
            answer *= int(string[i])
    return answer


if __name__ == '__main__':
    assert digitsmanip(123405) == 120
    assert digitsmanip(999) == 729
    assert digitsmanip(1000) == 1
    assert digitsmanip(1111) == 1
    print("Tests complete!")
