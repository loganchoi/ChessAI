# This is where you build your AI for the Chess game.

from ctypes import memmove
from time import time
from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
import random
import math
import time
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

        #Get TurnLimit which is (timeremaining/10**9)/60
        turnlimit = ((self.player.time_remaining)/10**9)/80
        print(turnlimit)
        move = (maxChoice(self.board,self.actual,inputs[1],turnlimit))
        print(move)
        return move
        '''
        #Get a random move and return
        move = random.choice(self.actual)
        print(move)
        print(self.actual)
        return move
        '''
        # <<-- /Creer-Merge: makeMove -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here

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


def checkBlackMoves(board,enpassant,castle):
    #Get Black Pieces Moves
    rook = [[-1,0],[1,0],[0,-1],[0,1]]
    knight = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
    bishop = [[-1,-1],[1,1],[1,-1],[-1,1]]
    valid_moves = []
    for x in range(0,8):
        for y in range(0,8):
            if board[x][y].islower():
                if board[x][y] == "p":
                    valid_moves = valid_moves + b_pawn_moves(board,x,y,enpassant)
                elif board[x][y] == "r":
                    valid_moves = valid_moves + b_other_moves(board,x,y,rook)
                elif board[x][y] == "n":
                    valid_moves = valid_moves + b_other_moves(board,x,y,knight,1)
                elif board[x][y] == "b":
                    valid_moves = valid_moves + b_other_moves(board,x,y,bishop)
                elif board[x][y] == "q":
                    valid_moves = valid_moves + b_other_moves(board,x,y,rook)
                    valid_moves = valid_moves + b_other_moves(board,x,y,bishop)
                elif board[x][y] == "k":
                    valid_moves = valid_moves + b_other_moves(board,x,y,rook,1)
                    valid_moves = valid_moves + b_other_moves(board,x,y,bishop,1)
                    valid_moves = valid_moves + b_castle(board,x,y,castle)  
    return valid_moves


def checkWhiteMoves(board,enpassant,castle):
    #Get White Piece Moves
    rook = [[-1,0],[1,0],[0,-1],[0,1]]
    knight = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
    bishop = [[-1,-1],[1,1],[1,-1],[-1,1]]
    valid_moves = []
    for x in range(0,8):
        for y in range(0,8):
            if board[x][y].isupper():
                if board[x][y] == "P":
                    valid_moves = valid_moves + w_pawn_moves(board,x,y,enpassant)
                elif board[x][y] == "R":
                    valid_moves = valid_moves + w_other_moves(board,x,y,rook)
                elif board[x][y] == "N":
                    valid_moves = valid_moves + w_other_moves(board,x,y,knight,1)
                elif board[x][y] == "B":
                    valid_moves = valid_moves + w_other_moves(board,x,y,bishop)
                elif board[x][y] == "Q":
                    valid_moves = valid_moves + w_other_moves(board,x,y,rook)
                    valid_moves = valid_moves + w_other_moves(board,x,y,bishop)
                elif board[x][y] == "K":
                    valid_moves = valid_moves + w_other_moves(board,x,y,rook,1)
                    valid_moves = valid_moves + w_other_moves(board,x,y,bishop,1)  
                    valid_moves  = valid_moves + w_castle(board,x,y,castle)   
    return valid_moves

#This gets the pawn promotions 
def pawn_promote(start,dest):
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
                p_moves = p_moves + pawn_promote(start,dest)
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
                p_moves = p_moves + pawn_promote(start,dest)
            else:
                p_moves.append(start+dest)
    
    #right capture or enpassant
    if bound_check(row-1,col-1):
        if convertSAN(row-1,col-1) in enpassant or board[row-1][col-1].islower():
            dest = convertSAN(row-1,col-1)
            if row-1 == 0:
                p_moves = p_moves + pawn_promote(start,dest)
            else:
                p_moves.append(start+dest)

    return p_moves

def w_other_moves(board,row,col,movements,range=7):
    #Go left,right,up,down
    all_moves = []
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
                    all_moves.append(start+dest)
                elif board[newRow][newCol].islower():
                    dest = convertSAN(newRow,newCol)
                    all_moves.append(start+dest)
                    break
                else:
                    break
            else:
                break

    return all_moves


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
                p_moves = p_moves + pawn_promote(start,dest)
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
                p_moves = p_moves + pawn_promote(start,dest)
            else:
                p_moves.append(start+dest)
    
    #right capture or enpassant
    if bound_check(row+1,col-1):
        if convertSAN(row+1,col-1)in enpassant or board[row+1][col-1].isupper():
            dest = convertSAN(row+1,col-1)
            if row+1 == 7:
                p_moves = p_moves + pawn_promote(start,dest)
            else:
                p_moves.append(start+dest)

    return p_moves

#Same as w_other_moves
def b_other_moves(board,row,col,movements,range=7):
    all_moves = []
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
                    all_moves.append(start+dest)
                elif board[newRow][newCol].isupper():
                    dest = convertSAN(newRow,newCol)
                    all_moves.append(start+dest)
                    break
                else:
                    break
            else:
                break

    return all_moves

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

#The terminal function just checks to see if a king has been taken and isn't on board
def terminal(board,ogColor):
    if abs(h_value(board,ogColor)) >= 1000:
        return True
    return False

#The h_value is the heuristic function that just calculates all the total pieces on the board
#relative to the perspective of the current player
def h_value(board,color):
    h = 0
    w_point = {"P":1,"N":3,"B":3,"R":5,"Q":9,"K":1000}
    b_point = {"p":1,"n":3,"b":3,"r":5,"q":9,"k":1000}
    for x in board:
        for y in x:
            if color == "w":
                if y in w_point.keys():
                    h = h + w_point[y]
                elif y in b_point.keys():
                    h = h - b_point[y]
            elif color == "b":
                if y in b_point.keys():
                    h = h + b_point[y]
                elif y in w_point.keys():
                    h = h - w_point[y]
            
    return h

#This just manually deepcopies a newboard with the position switched
def deepcopy(board,move):
    kings = ["k","K"]
    newBoard = [row[:] for row in board]
    s_row,s_col,e_row,e_col = moveTrans(move)
    newBoard[e_row][e_col] = newBoard[s_row][s_col]
    newBoard[s_row][s_col] = "0"
    if board[s_row][s_col] in kings and abs(e_col - s_col) == 2: #This is the castle move
        if s_col - e_col > 0: #queenside
             newBoard[s_row][3] =  newBoard[s_row][0] 
             newBoard[s_row][0] = "0"
        else:
             newBoard[s_row][5] = newBoard[s_row][7]
             newBoard[s_row][7] = "0"
    return newBoard

#This just starts the recursive call for the functions and does IDDL with timeout and Alpha-Beta Pruning
def maxChoice(board,moves,color,turnTime):
    t0 = time.time()
    alpha = -math.inf
    beta = math.inf
    available = []
    v = -math.inf
    depth = 1
    while True:
        for m in moves:
            newBoard = deepcopy(board,m)
            val = minValue(newBoard,depth,color,color,alpha,beta)
            if val == v:
                available.append(m)
            elif val > v:
                v = val
                available = [m]
        t1 = time.time()
        if t1 - t0 > turnTime/2:
            print("Broke at depth", depth, "with this much time", t1-t0)
            break
        depth = depth + 1


    return random.choice(available)

#This returns maxValue 
def maxValue(board,depth,color,ogColor,alpha,beta):
    switch_color = {"b":"w","w":"b"}
    if terminal(board,ogColor):
        return h_value(board,ogColor)
    if depth == 0:
        return h_value(board,ogColor)

    if color == 'w':
        valid_moves = checkBlackMoves(board,'','')
    else:
        valid_moves = checkWhiteMoves(board,'','')
    
    v = -math.inf
    for move in valid_moves:
        newBoard = deepcopy(board,move)
        val = minValue(newBoard,depth-1,switch_color[color],ogColor,alpha,beta)
        if val > v:
            v = val
        if v >= beta:
            return v
        alpha = max(alpha,v)
    
    return v

#This returns minValue
def minValue(board,depth,color,ogColor,alpha,beta):
    switch_color = {"b":"w","w":"b"}
    if terminal(board,ogColor):
        return h_value(board,ogColor)
    if depth == 0:
        return h_value(board,ogColor)

    if color == 'w':
        valid_moves = checkBlackMoves(board,'','')
    else:
        valid_moves = checkWhiteMoves(board,'','')
    
    v = math.inf
    for move in valid_moves:
        newBoard = deepcopy(board,move)
        val = maxValue(newBoard,depth-1,switch_color[color],ogColor,alpha,beta)
        if val < v:
            v = val
        if v <= alpha:
            return v
        beta = min(beta,v)
    
    return v

    # <<-- /Creer-Merge: functions -->>
