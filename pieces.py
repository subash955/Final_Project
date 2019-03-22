files = {1:'A', 2: 'B' , 3: 'C' ,4: 'D', 5: 'E', 6:'F', 7:'G', 8:'H'}
ranks = [1,2,3,4,5,6,7,8]

class Square:
    def __init__(self, file, rank):
        self.rank = rank
        self.file = file
        self.piece = 0

    def setpiece (self, piece):
        self.piece = piece
        
    def getpiece (self):
        if self.piece == 0:
            return '  '
        else:
            return self.piece
        
    def __str__(self):
        return (str(files[self.file]) + str(self.rank))
    
Board = [[x for x in ranks] for y in ranks]
for x in range (8):
    for y in range (8):
        Board[x][y] = Square(x+1,y+1)



class piece:
    
    def __init__ (self, color, file, rank):
        self.value = 0
        self.color = color
        self.position = Board[file-1][rank-1]
        Board[file-1][rank-1].piece = self
        

    def is_captured (self):
        self.position = 0

    def move (self, new_pos):
        self.position.setpiece(0)
        self.position = new_pos
        self.position.setpiece(self)    
        
    def capture (self, new_pos):
        if new_pos.piece != 0:
            new_pos.piece.is_captured()
            self.move(new_pos)
        else:
            print ("Error")
            
    def __str__(self):
        if self.color == 'w':
            return (self.w_name)
        else:
            return (self.b_name)
              
class pawn (piece):
    w_name = '♙'
    b_name = '♟'
    name = "P"
    def check_capture(self,new_pos):
        if self.color == 'w':
            if new_pos.rank == self.position.rank + 1 and abs(new_pos.file - self.position.file) == 1 and new_pos.piece != 0:
                if new_pos.piece.color != self.color:
                    return True
            return False
        else:
            if new_pos.rank == self.position.rank - 1 and abs(new_pos.file - self.position.file) == 1 and new_pos.piece != 0:
                if new_pos.piece.color != self.color:
                    return True
            return False
    
    def capture (self, new_pos):
        if self.check_capture(new_pos):
                new_pos.piece.is_captured()
                self.move(new_pos)
        else:
            print ("Error")
    
    def check_pawn_move(self,new_pos):
        if self.color == 'w':
            
            if self.position.rank == 2 and new_pos.file == self.position.file and new_pos.rank -2 == self.position.rank and new_pos.piece == 0 and Board[self.position.file-1][self.position.rank].piece == 0:
                return True
            if new_pos.file  != self.position.file or new_pos.rank - 1 != self.position.rank:
                    return False
            if  Board[self.position.file-1][self.position.rank].piece != 0:
                return False
            return True
        else: 
            if self.position.rank == 7 and new_pos.file == self.position.file and new_pos.rank +2 == self.position.rank:
                return True
            if new_pos.file  != self.position.file or new_pos.rank + 1 != self.position.rank:
                return False
            if  Board[self.position.file-1][self.position.rank-2].piece != 0:
                return False
            return True
        
    
    def move_piece (self, new_pos):
        if self.color == 'w':
            if self.check_capture(new_pos):
                self.capture(new_pos)
                if self.position.rank == 8:
                    self.promote()
            elif self.check_pawn_move(new_pos):
                if (new_pos.rank - 2 == 2):
                    self.move(Board[self.position.file-1][self.position.rank+1])
                else:
                    self.move(Board[self.position.file-1][self.position.rank])
                    if self.position.rank == 8:
                        self.promote()
        else:
            if self.check_capture(new_pos):
                self.capture(new_pos)
                if self.position.rank == 1:
                    self.promote()
            elif  self.check_pawn_move(new_pos):
                if (new_pos.rank + 2 == 7):
                    self.move(Board[self.position.file-1][self.position.rank-3])
                else:
                    self.move(Board[self.position.file-1][self.position.rank-2])
                    if self.position.rank == 1:
                        self.promote()
            
    def can_move(self):
        for x in Board:
            for y in x:
                if self.check_pawn_move(y) or self.check_capture(y):
                    return True
        return False
    
    def promote(self):
        self = Queen(self.color, self.position.file, self.position.rank)
    
    def check_move(self, new_pos):
        if self.check_pawn_move(new_pos) or self.check_capture(new_pos):
            return True
        return False

class Knight (piece):
    w_name = '♘'
    b_name = '♞'
    name = "N"
    def Check_Knight_Move (self, new_pos):
        valid_moves = [(1,2), (2,1), (-1,2),(1,-2), (-1,-2), (-2,-1), (2,-1), (-2,1)]
        for (x,y) in valid_moves:
            if self.position.rank + x == new_pos.rank and self.position.file + y == new_pos.file:
                if new_pos.piece == 0:
                    return True
                elif new_pos.piece.color == self.color:
                    return False
        return False
    
    def move_piece(self, new_pos):
        if self.Check_Knight_Move(new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    self.capture (new_pos)
            else:
                self.move(new_pos)
        else:
            print ("Error")
            
    def check_capture(self, new_pos):
        if self.Check_Knight_Move(new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False
    
    def can_move(self):
        for x in Board:
            for y in x:
                if self.Check_Knight_Move(y):
                    return True
        return False
    
    def check_move(self, new_pos):
        if self.Check_Knight_Move(new_pos):
            return True
        return False

class Bishop (piece):
    w_name = '♗'
    b_name = '♝'
    name = 'B'
    def check_bishop_move (self, new_pos):
        dx = new_pos.file - self.position.file
        dy = new_pos.rank - self.position.rank
        
        if abs(dx) != abs (dy):
            return False
        if dx == 0 or dy == 0:
            return False
        
        if new_pos.piece != 0:
            if new_pos.piece.color == self.color:
                return False
            
        if new_pos.piece != 0:
                if new_pos.piece.color == self.color:
                    return False
        if dx > 0 and dy > 0:
            for x ,y  in zip (range (1,dx),  range (1,dy)):
                if Board[self.position.file+x-1][self.position.rank+y-1].piece != 0:
                    
                    return False
            return True
        if dx < 0 and dy > 0:
            for x ,y  in zip (range (1,-dx),  range (1,dy)):
                if Board[self.position.file - x-1][self.position.rank+y-1].piece != 0:
                   
                    return False
            return True
        if dx > 0 and dy < 0:
            for x ,y  in zip (range (1,dx),  range (1,-dy)):
                if Board[self.position.file+x-1][self.position.rank-y-1].piece != 0:
                    
                    return False
            return True
        if dx < 0 and dy < 0:
            for x ,y  in zip (range (1,-dx),  range (1,-dy)):
                if Board[self.position.file-x-1][self.position.rank-y-1].piece != 0:
                    
                    return False
            return True
        
    def move_piece (self, new_pos):
        if self.check_bishop_move(new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print ("Error")
    
    def check_capture(self, new_pos):
        if self.check_bishop_move(new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False
    
    def can_move(self):
        for x in Board:
            for y in x:
                if self.check_bishop_move(y):
                    return True
        return False
    
    def check_move(self, new_pos):
        if self.check_bishop_move(new_pos):
            return True
        return False

class Rook (piece):
    w_name = '♖'
    b_name = '♜'
    name = 'R'
    def check_rook_move (self, new_pos):
        dx = new_pos.file - self.position.file
        dy = new_pos.rank - self.position.rank
        
        if dx != 0 and dy != 0:
            return False
        
        if new_pos.piece != 0:
            if new_pos.piece.color == self.color:
                return False
        
        if dx > 0:
            for x in range (1,dx):
                if Board[self.position.file-1+x][self.position.rank-1].piece != 0:
                    
                    return False
            return True
        if dy > 0:
            for y in range (1,dy):
                if Board[self.position.file-1][self.position.rank+y-1].piece != 0:
                
                    return False
            return True
        if dx < 0:
            for x in range (1,-dx):
                if Board[self.position.file-x-1][self.position.rank-1].piece != 0:
                  
                    return False
            return True
        if dy < 0:
            for y in range (1,-dy):
                if Board[self.position.file-1][self.position.rank-y-1].piece != 0:
                    
                    return False
            return True
    def move_piece (self, new_pos):
        if self.check_rook_move(new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print ("Error")
    
    def check_capture(self, new_pos):
        if self.check_rook_move(new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False
    
    def can_move(self):
        for x in Board:
            for y in x:
                if self.check_rook_move(y):
                    return True
        return False
    
    def check_move(self, new_pos):
        if self.check_rook_move(new_pos):
            return True
        return False
    
        
class Queen (Rook, Bishop):
    w_name = '♕'
    b_name = '♛'
    name = 'Q'
    def check_queen_move (self, new_pos):
        if self.check_rook_move( new_pos) or self.check_bishop_move(new_pos):
            return True
        else:
            return False
        
    def move_piece (self, new_pos):
        if self.check_queen_move(new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print ("Error")
            
    def check_capture(self, new_pos):
        if self.check_queen_move(new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False
    def can_move(self):
        for x in Board:
            for y in x:
                if self.check_queen_move(y):
                    return True
        return False
    def check_move(self, new_pos):
        if self.check_queen_move(new_pos):
            return True
        return False

class King (Queen):
    w_name = '♔'
    b_name = '♚'
    name = 'K'
    
    def check_legal(self,new_pos):
        z = new_pos.piece
        new_pos.piece = 0
        for x in Board:
            for y in x:
                if y.piece != 0:
                    if y.piece.color != self.color:
                        if y.piece.name == "K":
                                dx = new_pos.file - self.position.file
                                dy = new_pos.rank - self.position.rank
                                if dx <= 1 and dy <= 1:
                                    if y.piece.check_queen_move(new_pos):
                                        new_pos.piece = z
                                        return False
                        elif y.piece.name == "P":
                            if y.piece.color == 'w':
                                if new_pos.rank == y.piece.position.rank + 1 and abs(new_pos.file - y.piece.position.file) == 1:
                                    new_pos.piece = z
                                    return False
                            else:
                                if new_pos.rank == y.piece.position.rank - 1 and abs(new_pos.file - y.piece.position.file) == 1:
                                    new_pos.piece = z
                                    return False
                        else: 
                            if y.piece.check_move(new_pos):
                                new_pos.piece = z
                                return False
        new_pos.piece = z
        return True
    
    def check_king_move(self,new_pos):
        dx = new_pos.file - self.position.file
        dy = new_pos.rank - self.position.rank
        
        if dx > 1 or dy > 1:
            return False
        
        if self.check_queen_move(new_pos) and self.check_legal(new_pos):
            return True
        else: 
            return False
        
    def move_piece(self,new_pos):
        if self.check_king_move(new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print("Error")
            
    def check_capture(self, new_pos):
        if self.check_king_move(new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False
    
    def ischeck(self):
        for x in Board:
            for y in x:
                if y.piece != 0:
                    if y.piece.check_capture(self.position):
                        return True
        return False
    
    def can_move(self):
        for x in Board:
            for y in x:
                if self.check_king_move(y):
                    return True
        return False
    
    def check_move(self, new_pos):
        if self.check_king_move(new_pos):
            return True
        return False

def arrange ():
    for x in range (8):
        Board[x][1].setpiece (pawn('w',x+1,2))
        Board[x][6].setpiece (pawn('b',x+1,7))
    Board[0][0].setpiece(Rook('w', 1,1))
    Board[7][0].setpiece(Rook('w', 8,1))
    Board[7][7].setpiece(Rook('b', 8,8))
    Board[0][7].setpiece(Rook('b', 1,8))
    Board[1][0].setpiece(Knight('w',2,1))
    Board[6][0].setpiece(Knight('w',7,1))
    Board[1][7].setpiece(Knight('b',2,8))
    Board[6][7].setpiece(Knight('b',7,8))
    Board[2][0].setpiece(Bishop('w',3,1))
    Board[5][0].setpiece(Bishop('w',6,1))
    Board[2][7].setpiece(Bishop('b',3,8))
    Board[5][7].setpiece(Bishop('b',6,8))
    Board[3][0].setpiece(Queen('w',4,1))
    Board[3][7].setpiece(Queen('b',4,8))
    Board[4][0].setpiece(King('w',5,1))
    Board[4][7].setpiece(King('b',5,8))

def drawboard():
    num = [0,1,2,3,4,5,6,7]
    for x in Board:
        for y in x:
            print (('|' + str(y.getpiece())) + '|', end = '')
        print()

def playermove (color, bol):
    possible_moves = []
    print("These are the available pieces: ")
    if (bol):
        for x in Board:
            for y in x:
                if y.piece != 0:
                    if y.piece.color == color and y.piece.can_move() and y.piece.name == 'K':
                        possible_moves.append(y)
    else:
        for x in Board:
            for y in x:
                if y.piece != 0:
                    if y.piece.color == color and y.piece.can_move():
                        possible_moves.append(y)
    c = 1
    for y in possible_moves:
        print (str(c) + '. ' + y.piece.name + ' at '  + str(y.piece.position))
        c += 1
    num = int(input ("\nWhich piece would you like to move (number): "))
    possible_sq = []
    for x in Board:
        for y in x:
            if possible_moves[num - 1].piece.check_move(y):
                possible_sq.append(y)
    
    c= 1
    for x in possible_sq:
        print (str(c) + '. ' + str(x))
        c += 1
        
    num2 = int(input("\nWhere would you like to move it: "))
    
    possible_moves[num-1].piece.move_piece(possible_sq[num2-1])


def main():

    arrange() 
    bk = Board[4][7].piece
    wk = Board[4][0].piece

    c = 1
    
    while (1):
        drawboard()
        if c == 1:
            if wk.ischeck():
                playermove('w', True)
            else:
                playermove('w', False)
        else:
            if bk.ischeck():
                playermove('b', True)
            else:
                playermove('b', False)
        c = -c
        if bk.ischeck():
            if bk.can_move():
                pass
            else:
                print ("Game Over")
                break
        
        if wk.ischeck():
            if wk.can_move():
                pass
            else:
                print ("Game Over")
                break
        
main()