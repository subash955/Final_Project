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
        
class pawn (piece):
    
    def capture (self, new_pos):
        if new_pos.rank == self.position.rank + 1 and abs(new_pos.file - self.position.file) == 1 and new_pos.piece != 0:
            new_pos.piece.is_captured()
            self.move(new_pos)
        else:
            print ("Error")
        