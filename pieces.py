files = [A,B,C,D,E,F]
ranks = [1,2,3,4,5,6,7,8]

class Square:
    def __init__(self, file, rank):
        self.rank = rank
        self.file = file
        self.occupied = False

    def changeoccupy (self):
        self.occupied = !self.occupied
    
    def __str__(self):
        return (self.file + self.rank)

        
Board = [Square(x,y) for x in files for y in ranks]





	

