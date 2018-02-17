def mostnums(*args):
    """
    Finds the difference between the largest and smallest number
    :param args: List of numbers
    :return: Difference between largest and smallest
    
    """
    if not args:
        return 0
    else:
        return (max(args)-min(args))


if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(mostnums(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(mostnums(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(mostnums(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(mostnums(), 0, 3), "Empty"
