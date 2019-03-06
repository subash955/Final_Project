files = {1:'A', 2: 'B' , 3: 'C' ,4: 'D', 5: 'E', 6:'F', 7:'G', 8:'H'}
ranks = [1,2,3,4,5,6,7,8]

class Square:
    def __init__(self, file, rank):
        self.rank = rank
        self.file = file
        self.piece = 0

    def setpiece (self, piece):
        self.piece = piece
    
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
            return (self.name)
        else:
            return (self.name.lower())
            
class pawn (piece):
    name = 'P'
    def check_capture(self,new_pos):
        if new_pos.rank == self.position.rank + 1 and abs(new_pos.file - self.position.file) == 1 and new_pos.piece != 0:
            if new_pos.piece.color != self.color:
                return True
        return False
    def capture (self, new_pos):
        if self.check_capture(self,new_pos):
                new_pos.piece.is_captured()
                self.move(new_pos)
        else:
            print ("Error")
    
    def move_piece (self, new_pos):
        if self.position.rank < 7 and Board[self.position.file-1][self.position.rank].piece == 0:
            self.move(Board[self.position.file-1][self.position.rank])
        elif self.position.rank == 7 and Board[self.position.file-1][7] == 0:
            self.promote()
        else:
            print(error)
        
    
    def promote():
        pass

class Knight (piece):
    name = 'N'
    def Check_Knight_Move (self, new_pos):
        valid_moves = [(1,2), (2,1), (-1,2),(1,-2), (-1,-2), (-2,-1), (2,-1), (-2,1)]
        for (x,y) in valid_moves:
            if self.position.rank + x == new_pos.rank and self.position.file + y == new_pos.file:
                return True
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
        if self.Check_Knight_Move(self,new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False

class Bishop (piece):
    name = 'B'
    def check_bishop_move (self, new_pos):
        dx = new_pos.file - self.position.file
        dy = new_pos.rank - self.position.rank
        
        if abs(dx) != abs (dy):
            return False
        
        if new_pos.piece != 0:
                if new_pos.piece.color == self.color:
                    return False
        if dx > 0 and dy > 0:
            for x in range (dx), y in range (dy):
                if Board[self.position.file+x][self.position.rank+y].piece != 0:
                    print("Error")
                    return False
            return True
        if dx < 0 and dy > 0:
            for x in range (-dx), y in range (dy):
                if Board[self.position.file-x][self.position.rank+y].piece != 0:
                    print("Error")
                    return False
            return True
        if dx > 0 and dy < 0:
            for x in range (dx), y in range (-dy):
                if Board[self.position.file+x][self.position.rank-y].piece != 0:
                    print("Error")
                    return False
            return True
        if dx < 0 and dy < 0:
            for x in range (-dx), y in range (-dy):
                if Board[self.position.file-x][self.position.rank-y].piece != 0:
                    print("Error")
                    return False
            return True
        
    def move_piece (self, new_pos):
        if self.check_bishop_move(self,new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print ("Error")
    
    def check_capture(self, new_pos):
        if self.check_bishop_move(self,new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False

class Rook (piece):
    name = 'R'
    def check_rook_move (self, new_pos):
        dx = new_pos.file - self.position.file
        dy = new_pos.rank - self.position.rank
        
        if dx != 0 and dy != 0:
            return False
        
        if dx > 0:
            for x in range (dx):
                if Board[self.position.file+x][self.position.rank].piece != 0:
                    print("Error")
                    return False
            return True
        if dy > 0:
            for y in range (dy):
                if Board[self.position.file][self.position.rank+y].piece != 0:
                    print("Error")
                    return False
            return True
        if dx < 0:
            for x in range (-dx):
                if Board[self.position.file-x][self.position.rank].piece != 0:
                    print("Error")
                    return False
            return True
        if dy < 0:
            for y in range (-dy):
                if Board[self.position.file][self.position.rank-y].piece != 0:
                    print("Error")
                    return False
            return True
    def move_piece (self, new_pos):
        if self.check_rook_move(self,new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print ("Error")
    
    def check_capture(self, new_pos):
        if self.check_rook_move(self,new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False
        
class Queen (Rook, Bishop):
    name = 'Q'
    def check_queen_move (self, new_pos):
        if self.check_rook_move(self, new_pos) or self.check_bishop_move(self,new_pos):
            return True
        else:
            return False
        
    def move_piece (self, new_pos):
        if self.check_queen_move(self,new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print ("Error")
            
    def check_capture(self, new_pos):
        if self.check_queen_move(self,new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False
    
class King (Queen):
    name = 'K'
    def check_legal(self,new_pos):
        x = new_pos.piece
        new_pos.piece = self
        for x in Board:
            if x.piece.check_capture():
                return False
        new_pos.piece = x
        return True
    def check_king_move(self,new_pos):
        dx = new_pos.file - self.position.file
        dy = new_pos.rank - self.position.rank
        if dx > 1 or dy > 1:
            return False
        
        if check_queen_move(self,new_pos) and check_legal(self,new_pos):
            return True
        else: 
            return False
    def move_piece(self,new_pos):
        if self.check_king_move(self,new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print("Error")
            
    def check_capture(self, new_pos):
        if self.check_king_move(self,new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    return True
        return False
    
def arrange ():
    for x in range (8):
        Board[x][1].setpiece (pawn('w',x+1,2))
        Board[x][6].setpiece (pawn('b',x+1,2))
    Board[0][0].setpiece(Rook('w', 1,1))
    Board[7][0].setpiece(Rook('w', 8,1))
    Board[7][7].setpiece(Rook('b', 8,8))
    Board[0][7].setpiece(Rook('b', 1,8))
    Board[1][0].setpiece(Knight('w',2,1))
    Board[6][0].setpiece(Knight('w',7,1))
    Board[1][7].setpiece(Knight('b',2,8))
    Board[6][7].setpiece(Knight('w',7,8))
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
            print ((' | ' + str(y.piece)), end = ' ')
        print()
            


