"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    """
    if word in wordlist:
        return True
    else:
        return False


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

'
    """
    string = ""
    for i in range(len(board[row_index])):
        string = string + board[row_index][i]
    return string


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    """
    string = ""
    for i in range(len(board)):
        string = string + board[i][column_index]
    return string


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    """
    for i in range(len(board[0])):
        if word in make_str_from_column(board, i):
            return True

    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.


    """
    if board_contains_word_in_row(board, word):
        return True
    elif board_contains_word_in_column(board, word):
        return True
    return False


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    """
    x = len(word)
    if x < 3:
        return 0
    elif x >= 3 and x <= 6:
        return x
    elif x >= 7 and x <= 9:
        return x * 2
    else:
        return x * 3


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.


    """
    player_info[1] = player_info[1] + word_score(word)


def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    
    """
    c = 0
    for i in range(len(words)):
        if board_contains_word(board, words[i]):
            c += 1
    return c


