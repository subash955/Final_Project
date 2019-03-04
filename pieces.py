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
for x in range (7):
    for y in range (7):
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
            
class pawn (piece):
    
    def capture (self, new_pos):
        if new_pos.rank == self.position.rank + 1 and abs(new_pos.file - self.position.file) == 1 and new_pos.piece != 0:
            if new_pos.piece.color != self.color:
                new_pos.piece.is_captured()
                self.move(new_pos)
        else:
            print ("Error")
    def pawn_move (self):
        if self.position.rank < 7 and Board[self.position.file-1][self.position.rank].piece == 0:
            self.move(Board[self.position.file-1][self.position.rank])
        elif self.position.rank == 7 and Board[self.position.file-1][7] == 0:
            self.promote()
        else:
            print(error)
        
    
    def promote():
        pass

class Knight (piece):
    
    def Check_Knight_Move (self, new_pos):
        valid_moves = [(1,2), (2,1), (-1,2),(1,-2), (-1,-2), (-2,-1), (2,-1), (-2,1)]
        for (x,y) in valid_moves:
            if self.position.rank + x == new_pos.rank and self.position.file + y == new_pos.file:
                return True
        return False
    
    def move_knight(self, new_pos):
        if self.Check_Knight_Move(new_pos):
            if new_pos.piece!= 0:
                if new_pos.piece.color != self.color:
                    self.capture (new_pos)
            else:
                self.move(new_pos)
        else:
            print ("Error")

class Bishop (piece):
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
        
    def move_bishop (self, new_pos):
        if check_bishop_move(self,new_pos):
            if new_pos.piece == 0:
                self.move(new_pos)
            else:
                self.capture(new_pos)
        else:
            print ("Error")
            