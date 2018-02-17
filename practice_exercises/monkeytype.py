def count_words(text, words):
    """
    Check if string contains real words
    :param text: 
    :param words: 
    :return: Count of real words in string
    """
    count = 0
    for word in words: # probably should make words lowercase too
        if word in text.lower():
            count += 1
    return count


if __name__ == '__main__':
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Tests complete!")
