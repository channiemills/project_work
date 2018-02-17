def evenlast(array):
    """
        sums even-indexes elements and multiply by the last
    """
    temp_sum = 0
    for i in range(len(array)):
        if i%2 == 0:
            temp_sum += array[i]
    return 0 if not array else temp_sum*array[-1]


if __name__ == '__main__':
    assert evenlast([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert evenlast([1, 3, 5]) == 30, "(1+5)*5=30"
    assert evenlast([6]) == 36, "(6)*6=36"
    assert evenlast([]) == 0, "An empty array = 0"
    print("Tests complete!")
