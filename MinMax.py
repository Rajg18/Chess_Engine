import random
import time


pieceScore = {"K": 0, "Q": 90, "R": 50, "B": 35, "N": 30, "p": 10}

knightScore =  [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 3, 3, 3, 2, 1],
                [1, 2, 2, 2, 2, 2, 2, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]

bishopScore =  [[4, 3, 2, 1, 1, 2, 3, 4],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [2, 3, 4, 3, 3, 4, 3, 2],
                [3, 4, 3, 2, 2, 3, 4, 3],
                [4, 3, 2, 1, 1, 2, 3, 4]]

queenScore =   [[1, 1, 1, 3, 1, 1, 1, 1],
                [1, 2, 3, 3, 3, 1, 1, 1],
                [1, 4, 3, 3, 3, 4, 2, 1],
                [1, 2, 3, 3, 3, 2, 2, 1],
                [1, 2, 3, 3, 3, 2, 2, 1],
                [1, 4, 3, 3, 3, 4, 2, 1],
                [1, 2, 3, 3, 3, 1, 1, 1],
                [1, 1, 1, 3, 1, 1, 1, 1]]

rookScore =    [[4, 3, 4, 4, 4, 4, 3, 4],
                [4, 4, 4, 4, 4, 4, 4, 4],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 2, 3, 4, 4, 3, 2, 1],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [4, 4, 4, 4, 4, 4, 4, 4],
                [4, 3, 4, 4, 4, 4, 3, 4]]

whitePawnScore =   [[8, 8, 8, 8, 8, 8, 8, 8],
                    [8, 8, 8, 8, 8, 8, 8, 8],
                    [5, 6, 6, 7, 7, 6, 6, 5],
                    [2, 3, 3, 5, 5, 3, 3, 2],
                    [1, 2, 3, 4, 4, 3, 2, 1],
                    [1, 2, 3, 3, 3, 3, 2, 1],
                    [1, 1, 1, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

blackPawnScore =   [[0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 1, 1, 1],
                    [1, 2, 3, 3, 3, 3, 2, 1],
                    [1, 2, 3, 4, 4, 3, 2, 1],
                    [2, 3, 3, 5, 5, 3, 3, 2],
                    [5, 6, 6, 7, 7, 6, 6, 5],
                    [8, 8, 8, 8, 8, 8, 8, 8],
                    [8, 8, 8, 8, 8, 8, 8, 8]]

pawnEvalWhite = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [5, 5, 10, 25, 25, 10, 5, 5],
    [0, 0, 0, 20, 20, 0, 0, 0],
    [5, -5, -10, 0, 0, -10, -5, 5],
    [5, 10, 10, -20, -20, 10, 10, 5],
    [0, 0, 0, 0, 0, 0, 0, 0]
]


piecePosScores =  {'N': knightScore, 'B': bishopScore, 'Q': queenScore, 'R': rookScore, "wp": whitePawnScore, "bp": blackPawnScore}


CHECKMATE = 100000
STALEMATE = 0
MAX_DEPTH = 4

''' Find random move for AI '''
def findRandomMove(validMoves):
    if len(validMoves) > 0:
        return validMoves[random.randint(0, len(validMoves)-1)]


def findBestMoveMinimax(gs, validMoves, depth, alpha, beta, maximizingPlayer):
    bestMove = None
    if maximizingPlayer:
        maxEval = -float('inf')
        for move in validMoves:
            gs.makeMove(move)
            if depth == 1 or gs.checkMate or gs.staleMate:
                eval = evaluateBoard(gs)  # You should have an evaluation function
            else:
                nextMoves = gs.getValidMoves()
                eval = minimaxWithAlphaBeta(gs, nextMoves, depth - 1, alpha, beta, False)
            gs.undoMove()
            if eval > maxEval:
                maxEval = eval
                bestMove = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
    else:
        minEval = float('inf')
        for move in validMoves:
            gs.makeMove(move)
            if depth == 1 or gs.checkMate or gs.staleMate:
                eval = evaluateBoard(gs)
            else:
                nextMoves = gs.getValidMoves()
                eval = minimaxWithAlphaBeta(gs, nextMoves, depth - 1, alpha, beta, True)
            gs.undoMove()
            if eval < minEval:
                minEval = eval
                bestMove = move
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff

    return bestMove

def minimaxWithAlphaBeta(gs, validMoves, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or gs.checkMate or gs.staleMate:
        return evaluateBoard(gs)  # Evaluate the board state here

    if maximizingPlayer:
        maxEval = -float('inf')
        for move in validMoves:
            gs.makeMove(move)
            eval = minimaxWithAlphaBeta(gs, gs.getValidMoves(), depth - 1, alpha, beta, False)
            gs.undoMove()
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return maxEval
    else:
        minEval = float('inf')
        for move in validMoves:
            gs.makeMove(move)
            eval = minimaxWithAlphaBeta(gs, gs.getValidMoves(), depth - 1, alpha, beta, True)
            gs.undoMove()
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return minEval


def findMoveMinimax(gs, validMoves, depth, alpha, beta, whiteToMove):
    global nextMove
    global nodes
    nodes += 1
    if depth == 0 or gs.checkMate or gs.staleMate:
        return scoreBoard(gs)
    random.shuffle(validMoves)
    if whiteToMove:
        maxScore = -CHECKMATE
        random.shuffle(validMoves)
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinimax(gs, nextMoves, depth - 1, alpha, beta, False)
            gs.undoMove()
            if score > maxScore:
                maxScore = score
                if depth == MAX_DEPTH:
                    nextMove = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return maxScore
    else:
        minScore = CHECKMATE
        random.shuffle(validMoves)
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinimax(gs, nextMoves, depth - 1, alpha, beta, True)
            gs.undoMove()
            if score < minScore:
                minScore = score
                if depth == MAX_DEPTH:
                    nextMove = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return minScore

def scoreBoard(gs):
    if gs.checkMate:
        if gs.whiteToMove:
            return -CHECKMATE  #black win
        else:
            return CHECKMATE   #white win
    elif gs.staleMate:
        return STALEMATE
    # if not checkmate or stalemate:
    score = 0
    for row in range(8):
        for col in range(8):
            square = gs.board[row][col]
            if square != "--":
                piecePosScore = 0
                if square[1] != "K":
                    if square[1] == "p":
                        piecePosScore = piecePosScores[square][row][col]
                    else:
                        piecePosScore = piecePosScores[square[1]][row][col]
                if square[0] == 'w':
                    score += pieceScore[square[1]] + piecePosScore
                elif square[0] == 'b':
                    score -= pieceScore[square[1]] + piecePosScore
    return score


def evaluateBoard(gs):
    """
    Evaluates the board based on material value, positional factors, and king safety.
    """
    if gs.checkMate:
        if gs.whiteToMove:
            return -10000  # Black wins
        else:
            return 10000   # White wins
    elif gs.staleMate:
        return 0  # Draw

    materialScore = getMaterialScore(gs.board)
    positionScore = getPositionScore(gs.board, gs.whiteToMove)

    return materialScore + positionScore

def getMaterialScore(board):
    """
    Calculates the score based on material balance.
    """
    pieceValues = {
        'K': 0, 'Q': 900, 'R': 500, 'B': 330, 'N': 320, 'P': 100,  # White pieces
        'k': 0, 'q': -900, 'r': -500, 'b': -330, 'n': -320, 'p': -100,  # Black pieces
        'wK': 0, 'wQ': 900, 'wR': 500, 'wB': 330, 'wN': 320, 'wp': 100,  # White prefixed pieces
        'bK': 0, 'bQ': -900, 'bR': -500, 'bB': -330, 'bN': -320, 'bp': -100  # Black prefixed pieces
    }

    score = 0
    for row in board:
        for piece in row:
            if piece != "--":
                score += pieceValues[piece]

    return score


def getPositionScore(board, whiteToMove):
    """
    Position scoring based on piece position and influence.
    """
    score = 0
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece == 'P':  # White Pawn
                score += pawnEvalWhite[r][c]
            # Add other pieces (knights, rooks, etc.) similarly
    return score

