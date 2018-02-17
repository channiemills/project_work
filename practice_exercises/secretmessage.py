def find_message(text):
    """
    Find a secret message by extracting capital letters.
    """
    s = ""
    for i in text:
        if i.isupper():
            s+= i
    return s

if __name__ == '__main__':
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Tests complete!")
