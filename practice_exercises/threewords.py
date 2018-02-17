def threewords(words):
    """
    Check if string contains three words in succession
    :param words: 
    :return: True or false
    """
    count = 0
    for i in words.split():
        if i.isalpha():
            count += 1
            if count == 3: return True
        else:
            count = 0
    return False


if __name__ == '__main__':
    assert threewords("Hello World hello") == True, "Hello"
    assert threewords("He is 123 man") == False, "123 man"
    assert threewords("1 2 3 4") == False, "Digits"
    assert threewords("bla bla bla bla") == True, "Bla Bla"
    assert threewords("Hi") == False, "Hi"
    print("Tests complete!")
