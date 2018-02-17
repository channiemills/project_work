from collections import Counter


def nonuniqueelem(data):
    """
    Find only non-unique elements in provided list
    :param data: 
    :return: Non-unique elements
    """
    count_data = Counter(data)
    unique_keys = [k for k,v in count_data.items() if count_data[k] == 1]
    nonunique = [k for k in data if k not in unique_keys]
    return nonunique


if __name__ == "__main__":
    assert list(nonuniqueelem([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(nonuniqueelem([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(nonuniqueelem([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(nonuniqueelem([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("Tests complete!")
