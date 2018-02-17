def safe_pawns(pawns):
    """
    Count the number of safe pawns, those in a position where another pawn can claim its space if taken.
    :param pawns: 
    :return: Count of same pawns
    """
    safe_count = 0
    # for each square in pawns,
    for pawn in pawns:
        # if there is another square in pawns that is one file left or right of it and one row behind
        left = chr(ord(pawn[0]) - 1) + str(
            int(pawn[1]) - 1)  # probably want to add some checks to make sure left/right don't go off board
        right = chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1)
        if left in pawns or right in pawns:
            # count
            safe_count += 1
    return safe_count


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Tests complete!")
