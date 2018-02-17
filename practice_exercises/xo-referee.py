def xoref(game_result):
    """
    Determine who won a tic-tac-toe game based on score provided
    :param game_result: 
    :return: Who won or if it was a draw.
    """
    # could do elif for each condition, or just define them ahead of time
    if (game_result[0][0] == game_result[1][1] == game_result[2][2]) and (game_result[0][0] in ("X", "O")): #NWSE diagonal
        return game_result[0][0]
    if (game_result[0][2] == game_result[1][1] == game_result[2][0]) and (game_result[0][2] in ("X", "O")): #NESW diagonal
        return game_result[0][2]
    for row in range(3): # hold row constant and go through columns
            if (game_result[row][0] == game_result[row][1] == game_result[row][2]) and (game_result[row][0] in ("X", "O")):
                return game_result[row][0]
    for col in range(3): # hold column constant and go through rows
            if (game_result[0][col] == game_result[1][col] == game_result[2][col]) and (game_result[0][col] in ("X", "O")):
                return game_result[row][col]
    return "D"

if __name__ == '__main__':
    assert xoref([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert xoref([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert xoref([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert xoref([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Tests complete?!")
