def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    count = 0 # count of consecutive characters
    counter = [] # array tracking the max consecutive counts
    val = None # value of the character in the string
    for i in line:
        if val is None:
            val = i
        if val == i:
            count += 1
        else:
            counter.append(count)
            count = 1
            val = i
    return max(counter) if len(counter) != 0 else count


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('Tests complete!')
