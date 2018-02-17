def my_min(*args, **kwargs):
    """
    Replicates internal min function
    :param args: 
    :param kwargs: 
    :return: Returns min in provided list
    """
    key = kwargs.get("key", lambda x: x)
    dta = args[0] if len(args) == 1 else args[:]
    temp_min = None
    for i in dta:
        if temp_min == None:
            temp_min = i
        if key(i) < key(temp_min):
            temp_min = i
    return temp_min


def my_max(*args, **kwargs):
    """
    Replicates internal max function
    :param args: 
    :param kwargs: 
    :return: Returns max in provided list
    """
    key = kwargs.get("key", lambda x: x)
    dta = args[0] if len(args) == 1 else args[:]
    temp_max = None
    for i in dta:
        if temp_max == None:
            temp_max = i
        if key(i) > key(temp_max):
            temp_max = i
    return temp_max

if __name__ == '__main__':
    assert my_max(3, 2) == 3, "Simple case max"
    assert my_min(3, 2) == 2, "Simple case min"
    assert my_max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert my_min("hello") == "e", "From string"
    assert my_max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert my_min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Tests complete!")
