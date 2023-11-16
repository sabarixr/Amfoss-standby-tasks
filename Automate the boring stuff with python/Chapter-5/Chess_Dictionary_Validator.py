def isValidChessBoard(board):
    color = ['w', 'b']
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    white_pieces = 0
    black_pieces = 0
    piece_counts = {'wpawn': 0, 'wknight': 0, 'wbishop': 0, 'wrook': 0, 'wqueen': 0, 'wking': 0,
                    'bpawn': 0, 'bknight': 0, 'bbishop': 0, 'brook': 0, 'bqueen': 0, 'bking': 0}

    piece_limit = {'wpawn': 8, 'wknight': 2, 'wbishop': 2, 'wrook': 2, 'wqueen': 1, 'wking': 1,
                   'bpawn': 8, 'bknight': 2, 'bbishop': 2, 'brook': 2, 'bqueen': 1, 'bking': 1}
    possible_spaces = []
    possible_pieces = []
    for sp in letter:
        for i in range(1, 9):
            accepted_space = str(i) + sp
            possible_spaces.append(accepted_space)
    for pos_pic in color:
        for j in pieces:
            accepted_piece = pos_pic + j
            possible_pieces.append(accepted_piece)
    # print(possible_spaces)
    # print(possible_pieces)

    for space in board.keys():
        if space not in possible_spaces:
            print("The Chess board squares doesn't match chess standard")
            return False
    for piece in board.values():
        if piece == '':
            continue
        if piece not in possible_pieces:
            print(piece)
            print("The pieces provided doesn't match chess standard")
            return False
        else:
            piece_counts[piece] += 1

    for k in board.values():
        if k == '':
            continue
        if k[0] == 'w':
            white_pieces += 1

        elif k[0] == 'b':
            black_pieces += 1

    for pc, cnt in piece_counts.items():
        if cnt > piece_limit[pc]:
            print(f"Invalid number of {pc}")
            return False

    # print(white_pieces)
    # print(black_pieces)
    if black_pieces > 16:
        print("The number of black pieces shouldn't be more than 16")
        return False
    if white_pieces > 16:
        print("The number of white pieces shouldn't be more than 16")
        return False

    return True


board = {'1a': 'bking', '2a': 'bqueen', '3a': 'brook', '4a': 'brook',
         '5a': 'bknight', '6a': 'bknight', '7a': 'bbishop', '8a': 'bbishop',
         '1b': 'bpawn', '2b': 'bpawn', '3b': 'bpawn', '4b': 'bpawn',
         '5b': 'bpawn', '6b': 'bpawn', '7b': 'bpawn', '8b': 'bpawn',
         '1c': 'wking', '2c': 'wqueen', '3c': 'wrook', '4c': 'wrook',
         '5c': 'wbishop', '6c': 'wbishop', '7c': 'wknight', '8c': 'wknight',
         '1d': '', '2d': '', '3d': '', '4d': '', '5d': '', '6d': '', '7d': '', '8d': '',
         '1e': 'wpawn', '2e': 'wpawn', '3e': 'wpawn', '4e': 'wpawn',
         '5e': 'wpawn', '6e': 'wpawn', '7e': 'wpawn', '8e': 'wpawn',
         '1f': '', '2f': '', '3f': '', '4f': '', '5f': '', '6f': '', '7f': '', '8f': '',
         '1g': '', '2g': '', '3g': '', '4g': '', '5g': '', '6g': '', '7g': '', '8g': '',
         '1h': '', '2h': '', '3h': '', '4h': '', '5h': '', '6h': '', '7h': '', '8h': '', }

isValidChessBoard(board)

# maybe not the efficient code but i tried to use all the methods to do this
