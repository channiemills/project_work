def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    s = ","
    phrases = s.join(phrases)
    return phrases.replace('right', 'left')


if __name__ == '__main__':
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Tests complete!")
