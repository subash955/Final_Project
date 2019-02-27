files = [1: 'A', 2: 'B' , 3: 'C' ,4: 'D', 5: 'E', 6:'F', 7:'G', 8:'H']
ranks = [1,2,3,4,5,6,7,8]

class Square:
    def __init__(self, file, rank):
        self.rank = rank
        self.file = file
        self.piece = 0

    def setpiece (self, piece):
    	self.piece = piece
    
    def __str__(self):
        return (files[self.file] + self.rank)

        
#Board = [Square(x,y) for x in files for y in ranks]


class piece:
	
	def __init__ (self, color):
		self.value = 0
		self.color = color
		self.position = Square()

	def is_captured (self):
		self.status = False

	def move (self, new_pos):
		position.setpiece(0)
		position = new_pos
		position.changeoccupy(self)	
        
class pawn (piece):
    
    def capture (self, new_pos):
 		if new_pos.rank == self.position.rank + 1 and abs(new_pos.file - self.position.file) == 1:
 			self.move(new_pos)
 		else:
 			print ("Error")
 		





	

