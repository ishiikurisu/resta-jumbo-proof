from copy import deepcopy


def compact_board(board):
    outlet = ""
    for line in board:
        for square in line:
            piece = " "
            if square is True:
                piece = "x"
            elif square is False:
                piece = "."
            outlet += piece
        outlet += "\n"
    return outlet


def copy_board(board):
    outlet = []

    for line in board:
        box = []
        for piece in line:
            box.append(piece)
        outlet.append(box)

    return outlet


def within_limits(board, x, y):
    return x >= 0 and y >= 0 and x < len(board[0]) and y < len(board)


def is_possible_outcome(board, x, y, x1, y1, x2, y2):
    possible_outcome = None

    if within_limits(board, x2, y2) and board[y1][x1] is False and board[y2][x2] is False:
        possible_outcome = deepcopy(board)
        possible_outcome[y][x] = False
        possible_outcome[y1][x1] = True
        possible_outcome[y2][x2] = True

    return possible_outcome


def generate_possible_movements(board, piece):
    possible_outcomes = []
    x, y = piece[0], piece[1]

    options = [
        # x1, y1, x2, y2
        [x+1, y, x+2, y], # right
        [x-1, y, x-2, y], # left
        [x, y-1, x, y-2], # up
        [x, y+1, x, y+2], # down
    ]

    possible_outcomes = [
        option
        for option in [
            is_possible_outcome(board, x, y, x1, y1, x2, y2)
            for x1, y1, x2, y2 in options
        ]
        if option is not None
    ]

    return possible_outcomes


def generate_next_boards(board):
    # identifying pieces' positions
    pieces = []
    for j, line in enumerate(board):
        for i, square in enumerate(line):
            if square is True:
                pieces.append([i, j])

    # generating all possible following states for each piece
    outlet = []
    for piece in pieces:
        possible_outcomes = generate_possible_movements(board, piece)
        for possible_outcome in possible_outcomes:
            outlet.append(possible_outcome)

    return outlet


def is_victory(board):
    for line in board:
        for piece in line:
            if piece is False:
                return False
    return True


def play(board):
    possible_outcomes = generate_next_boards(board)
    if len(possible_outcomes) == 0:
        return is_victory(board)

    for possible_outcome in possible_outcomes:
        if play(possible_outcome):
            # print("---")
            # print compact_board(possible_outcome)
            return True
    return False


def main():
    board = [
        [None,  None,  False, False, False, None,  None ],
        [None,  None,  False, False, False, None,  None ],
        [False, False, False, False, False, False, False],
        [False, False, False, True,  False, False, False],
        [False, False, False, False, False, False, False],
        [None,  None,  False, False, False, None,  None ],
        [None,  None,  False, False, False, None,  None ],
    ]

    result = play(board)
    print(result)


if __name__ == '__main__':
    main()
