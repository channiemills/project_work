from collections import Counter


def mostwantedletter(text):
    """
    Finds the most frequent letter in lower case as a string
    :param text: 
    :return: Most frequent letter
    """
    temp = Counter(text.lower())
    alpha_keys = {k:temp[k] for k,v in temp.items() if k.isalpha()}
    max_keys = [k for k,v in alpha_keys.items() if alpha_keys[k] == max(alpha_keys.values())]
    if len(max_keys) == 1:
        return max_keys[0]
    else:
        return min(max_keys)


if __name__ == '__main__':
    assert mostwantedletter("Hello World!") == "l", "Hello test"
    assert mostwantedletter("How do you do?") == "o", "O is most wanted"
    assert mostwantedletter("One") == "e", "All letter only once."
    assert mostwantedletter("Oops!") == "o", "Don't forget about lower case."
    assert mostwantedletter("AAaooo!!!!") == "a", "Only letters."
    assert mostwantedletter("abe") == "a", "The First."
    print("Start the long test")
    assert mostwantedletter("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
