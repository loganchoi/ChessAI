# This is where you build your AI for the Chess game.

from ctypes import memmove
from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
import random
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Chess. """

    @property
    def game(self) -> 'games.chess.game.Game':
        """games.chess.game.Game: The reference to the Game instance this AI is playing.
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self) -> 'games.chess.player.Player':
        """games.chess.player.Player: The reference to the Player this AI controls in the Game.
        """
        return self._player # don't directly touch this "private" variable pls

    """
    print_board just outputs board so user can see it on terminal
    """
    def print_board(self,board):
        for x in range(0,8):
            for y in range(0,8):
                print(board[x][y],end="")
            print()

    """
    get_board is called to fill out the board from the fen string
    """
    def get_board(self,board_str):
        board = []
        row = 0
        col = 0
        emptyRow = []
        for c in board_str:
            if c.isalpha():
                emptyRow.append(c)
            elif c.isdigit():
                for x in range(0,int(c)):
                    emptyRow.append('0')
            elif c == '/':
                board.append(emptyRow)
                emptyRow = []
        board.append(emptyRow)
        return board
    
    def get_name(self) -> str:
        """This is the name you send to the server so your AI will control the player named this string.

        Returns:
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Logan Choi" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self) -> None:
        """This is called once the game starts and your AI knows its player and game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # <<-- /Creer-Merge: start -->>

    def game_updated(self) -> None:
        """This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won: bool, reason: str) -> None:
        """This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def make_move(self) -> str:
        """This is called every time it is this AI.player's turn to make a move.

        Returns:
            str: A string in Universal Chess Interface (UCI) or Standard Algebraic Notation (SAN) formatting for the move you want to make. If the move is invalid or not properly formatted you will lose the game.
        """
        # <<-- Creer-Merge: makeMove -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for makeMove

        #Get board/state first of course.
        #I will keep getting the new state by calling the fen string to generate the state
        inputs = self.game.fen.split()
        self.board = self.get_board(inputs[0])
        #This will hold the valid moves
        self.valid_moves = []

        #Check if it is white's or black's turn and get valid moves 
        if inputs[1] == "b":
            self.valid_moves = checkBlackMoves(self.board,inputs[3],inputs[2])
        else:
            self.valid_moves = checkWhiteMoves(self.board,inputs[3],inputs[2])
        
        #After gettiing valid possible moves, see if it puts the king in check
        self.actual = []
        for x in self.valid_moves:
            if legal_move(self.board,x,inputs[1]):
                self.actual.append(x)

        #Get a random move and return
        move = random.choice(self.actual)
        print(move)
        print(self.actual)
        return move
        # <<-- /Creer-Merge: makeMove -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here

def checkBlackMoves(board,enpassant,castle):
    #Get Black Pieces Moves
    valid_moves = []
    for x in range(0,8):
        for y in range(0,8):
            if board[x][y].islower():
                if board[x][y] == "p":
                    valid_moves = valid_moves + b_pawn_moves(board,x,y,enpassant)
                elif board[x][y] == "r":
                    valid_moves = valid_moves + b_rook_moves(board,x,y)
                elif board[x][y] == "n":
                    valid_moves = valid_moves + b_knight_moves(board,x,y)
                elif board[x][y] == "b":
                    valid_moves = valid_moves + b_bishop_moves(board,x,y)
                elif board[x][y] == "q":
                    valid_moves = valid_moves + b_bishop_moves(board,x,y)
                    valid_moves = valid_moves + b_rook_moves(board,x,y)
                elif board[x][y] == "k":
                    valid_moves = valid_moves + b_bishop_moves(board,x,y,1)
                    valid_moves = valid_moves + b_rook_moves(board,x,y,1)
                    valid_moves = valid_moves + b_castle(board,x,y,castle)  
    return valid_moves


def checkWhiteMoves(board,enpassant,castle):
    #Get White Piece Moves
    valid_moves = []
    for x in range(0,8):
        for y in range(0,8):
            if board[x][y].isupper():
                if board[x][y] == "P":
                    valid_moves = valid_moves + w_pawn_moves(board,x,y,enpassant)
                elif board[x][y] == "R":
                    valid_moves = valid_moves + w_rook_moves(board,x,y)
                elif board[x][y] == "N":
                    valid_moves = valid_moves + w_knight_moves(board,x,y)
                elif board[x][y] == "B":
                    valid_moves = valid_moves + w_bishop_moves(board,x,y)
                elif board[x][y] == "Q":
                    valid_moves = valid_moves + w_bishop_moves(board,x,y)
                    valid_moves = valid_moves + w_rook_moves(board,x,y)
                elif board[x][y] == "K":
                    valid_moves = valid_moves + w_bishop_moves(board,x,y,1)
                    valid_moves = valid_moves + w_rook_moves(board,x,y,1)  
                    valid_moves  = valid_moves + w_castle(board,x,y,castle)   
    return valid_moves

#This function checks if the row and col are in valid coordinates
def bound_check(x,y):
    if 0<= x <= 7 and 0<= y <=7:
        return True
    return  False

def convertSAN(row,col):
    #converts row,col to the corresponding SAN coordinates
    num = str(row*-1 + 8)
    let = chr(col +97)
    return let+num

#This function translates SAN back to row and col numberss
def moveTrans(move):
    start = move[0:2]
    end = move[2:4]
    s_row = (int(start[1]) - 8) * -1
    s_col = ord(start[0]) - 97
    e_row = (int(end[1]) - 8) * -1
    e_col = ord(end[0]) - 97
    return s_row,s_col,e_row,e_col

#This gets the pawn promotions 
def pawn_promote(start,dest,color):
    if color == "w":
        return [start+dest+'Q',start+dest+'R',start+dest+'N',start+dest+'B']
    else:
        return [start+dest+'q',start+dest+'r',start+dest+'n',start+dest+'b']

#This gets the white pawn moves
def w_pawn_moves(board,row,col,enpassant):
    start = convertSAN(row,col)
    p_moves = []

    #This just moves it one space forward if it is open
    if bound_check(row-1,col):
        if board[row-1][col]=='0':
            dest = convertSAN(row-1,col)
            if row-1 == 0:
                p_moves = p_moves + pawn_promote(start,dest,"w")
            else:
                p_moves.append(start+dest)
    #If the pawn is in starting position, you can move it forward twice
    if row == 6 and board[row-2][col] == "0" and board[row-1][col] == "0":
        dest = convertSAN(row-2,col)
        p_moves.append(start+dest)

    #left capture  or enpassant
    if bound_check(row-1,col+1):
        if convertSAN(row-1,col+1) in enpassant or board[row-1][col+1].islower():
            dest = convertSAN(row-1,col+1)
            if row-1 == 0:
                p_moves = p_moves + pawn_promote(start,dest,"w")
            else:
                p_moves.append(start+dest)
    
    #right capture or enpassant
    if bound_check(row-1,col-1):
        if convertSAN(row-1,col-1) in enpassant or board[row-1][col-1].islower():
            dest = convertSAN(row-1,col-1)
            if row-1 == 0:
                p_moves = p_moves + pawn_promote(start,dest,"w")
            else:
                p_moves.append(start+dest)

    return p_moves

def w_rook_moves(board,row,col,range=7):
    #Go left,right,up,down
    r_moves = []
    movements = [[-1,0],[1,0],[0,-1],[0,1]]
    start = convertSAN(row,col)
    #Continuously move north,south,east,west, and see if it is available
    #Available if it is an enemy piece or empty
    for move in movements:
        newRow = row
        newCol = col
        spaces = 0
        while spaces < range:
            newRow = newRow + move[0]
            newCol = newCol + move[1]
            spaces = spaces + 1
            if bound_check(newRow,newCol):
                if board[newRow][newCol] == '0':
                    dest = convertSAN(newRow,newCol)
                    r_moves.append(start+dest)
                elif board[newRow][newCol].islower():
                    dest = convertSAN(newRow,newCol)
                    r_moves.append(start+dest)
                    break
                else:
                    break
            else:
                break

    return r_moves

#Same thing as rook movements but different move sets
def w_knight_moves(board,row,col):
    start = convertSAN(row,col)
    k_moves = []
    movements = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
    for move in movements:
        newRow = row + move[0]
        newCol = col + move[1]
        if bound_check(newRow,newCol):
            if board[newRow][newCol] == '0' or board[newRow][newCol].islower():
                dest = convertSAN(newRow,newCol)
                k_moves.append(start+dest)
    return k_moves

#Same thing as rook movements but different move sets
def w_bishop_moves(board,row,col,range=7):
    b_moves = []
    movements = [[-1,-1],[1,1],[1,-1],[-1,1]]
    start = convertSAN(row,col)
    for move in movements:
        newRow = row
        newCol = col
        spaces = 0
        while spaces < range:
            newRow = newRow + move[0]
            newCol = newCol + move[1]
            spaces = spaces + 1
            if bound_check(newRow,newCol):
                if board[newRow][newCol] == '0':
                    dest = convertSAN(newRow,newCol)
                    b_moves.append(start+dest)
                elif board[newRow][newCol].islower():
                    dest = convertSAN(newRow,newCol)
                    b_moves.append(start+dest)
                    break
                else:
                    break
            else:
                break

    return b_moves


def w_castle(board,row,col,castle):
    #Check Long Side Castle (Queen) and Short Side Castle (King)
    wc_moves = []
    start = convertSAN(row,col)
    #Queenside
    if "Q" in castle and board[row][col-1] == '0' and board[row][col-2] == '0' and board[row][col-3] == '0':
        dest = convertSAN(row,col-2)
        wc_moves.append(start+dest)
    #Kingside
    if "K" in castle and board[row][col+1] == '0' and board[row][col+2] == '0':
        dest = convertSAN(row,col+2)
        wc_moves.append(start+dest)

    return wc_moves

#Same as w_pawn_moves
def b_pawn_moves(board,row,col,enpassant):
    start = convertSAN(row,col)
    p_moves = []
    if bound_check(row+1,col):
        if board[row+1][col]=='0':
            dest = convertSAN(row+1,col)
            if row+1 == 7:
                p_moves = p_moves + pawn_promote(start,dest,"b")
            else:
                p_moves.append(start+dest)

    if row == 1 and board[row+2][col] == "0" and board[row+1][col] == "0":
        dest = convertSAN(row+2,col)
        p_moves.append(start+dest)

    #left capture  or enpassant
    if bound_check(row+1,col+1):
        if convertSAN(row+1,col+1) in enpassant or board[row+1][col+1].isupper():
            dest = convertSAN(row+1,col+1)
            if row+1 == 7:
                p_moves = p_moves + pawn_promote(start,dest,"b")
            else:
                p_moves.append(start+dest)
    
    #right capture or enpassant
    if bound_check(row+1,col-1):
        if convertSAN(row+1,col-1)in enpassant or board[row+1][col-1].isupper():
            dest = convertSAN(row+1,col-1)
            if row+1 == 7:
                p_moves = p_moves + pawn_promote(start,dest,"b")
            else:
                p_moves.append(start+dest)

    return p_moves

#Same as w_rook_moves
def b_rook_moves(board,row,col,range=7):
    r_moves = []
    movements = [[-1,0],[1,0],[0,-1],[0,1]]
    start = convertSAN(row,col)
    for move in movements:
        newRow = row
        newCol = col
        spaces = 0
        while spaces < range:
            newRow = newRow + move[0]
            newCol = newCol + move[1]
            spaces = spaces + 1
            if bound_check(newRow,newCol):
                if board[newRow][newCol] == '0':
                    dest = convertSAN(newRow,newCol)
                    r_moves.append(start+dest)
                elif board[newRow][newCol].isupper():
                    dest = convertSAN(newRow,newCol)
                    r_moves.append(start+dest)
                    break
                else:
                    break
            else:
                break

    return r_moves

#Same as w_knight_moves
def b_knight_moves(board,row,col):
    start = convertSAN(row,col)
    k_moves = []
    movements = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
    for move in movements:
        newRow = row + move[0]
        newCol = col + move[1]
        if bound_check(newRow,newCol):
            if board[newRow][newCol] == '0' or board[newRow][newCol].isupper():
                dest = convertSAN(newRow,newCol)
                k_moves.append(start+dest)
    return k_moves

#Same as w_bishop_moves
def b_bishop_moves(board,row,col,range=7):
    b_moves = []
    movements = [[-1,-1],[1,1],[1,-1],[-1,1]]
    start = convertSAN(row,col)
    for move in movements:
        newRow = row
        newCol = col
        spaces = 0
        while spaces < range:
            newRow = newRow + move[0]
            newCol = newCol + move[1]
            spaces = spaces + 1
            if bound_check(newRow,newCol):
                if board[newRow][newCol] == '0':
                    dest = convertSAN(newRow,newCol)
                    b_moves.append(start+dest)
                elif board[newRow][newCol].isupper():
                    dest = convertSAN(newRow,newCol)
                    b_moves.append(start+dest)
                    break
                else:
                    break
            else:
                break

    return b_moves

#Same as w_castle 
def b_castle(board,row,col,castle):
    bc_moves = []
    start = convertSAN(row,col)
    if "q" in castle and board[row][col-1] == '0' and board[row][col-2] == '0' and board[row][col-3] == '0':
        dest = convertSAN(row,col-2)
        bc_moves.append(start+dest)
    if "k" in castle and board[row][col+1] == '0' and board[row][col+2] == '0':
        dest = convertSAN(row,col+2)
        bc_moves.append(start+dest)
        
    return bc_moves

#Find the king's position to check f
def findKing(newBoard,color):
    for x in range (0,8):
        for y in range(0,8):
            if color == "w":
                if newBoard[x][y] == "K":
                    return x,y
            if color ==  "b":
                if newBoard[x][y] == "k":
                    return x,y

def legal_move(board,move,color):
    #Check if the move makes the king in check 
    #Return False if king is in check
    #Return True if king isn't in check
    k_letter = ["K","k"]
    newBoard = [row[:] for row in board]
    s_row,s_col,e_row,e_col = moveTrans(move)

    #This checks only castling movements
    if newBoard[s_row][s_col] in k_letter and abs(s_col - e_col) == 2:
        king = convertSAN(s_row,s_col)
        if color == 'w':
            valid_moves = checkBlackMoves(newBoard,"","")
        else:
            valid_moves = checkWhiteMoves(newBoard,"","")
        if s_col - e_col > 0: #Queenside Castle
            for x in  valid_moves:
                #Check if any of the king spaces are being attacked
                if convertSAN(s_row,s_col) in x or convertSAN(s_row,s_col-1) in x or convertSAN(s_row,s_col-2) in x:
                    return False
            return True
        elif s_col - e_col < 0: #Kingside Castle
            for x in  valid_moves:
                #Check if any of the king spaces are being attacked
                if convertSAN(s_row,s_col) in x or convertSAN(s_row,s_col+1) in x or convertSAN(s_row,s_col+2) in x:
                    return  False
            return True
    #Otherwise it's just a regular normal move, so just check accordingly
    else:
        newBoard[e_row][e_col] = newBoard[s_row][s_col]
        newBoard[s_row][s_col] = '0'

        kingRow,kingCol = findKing(newBoard,color)
        king = convertSAN(kingRow,kingCol)

        if color == 'w':
            valid_moves = checkBlackMoves(newBoard,"","")
        else:
            valid_moves = checkWhiteMoves(newBoard,"","")
        
        for x in valid_moves:
            if king in x:
                return False

        return True

    # <<-- /Creer-Merge: functions -->>
