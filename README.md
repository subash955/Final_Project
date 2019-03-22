# Chess with Python

This is a program that allows the user to play chess against a human opponent on the same computer. The game contains all of the basic functionalities of chess such as checkmates, checks and captures. It automatically ends when the conditions have been met. 

## Installation

Download the zip file and run the file pieces.py, the game should start then. After each game, the program must be re-run in order to reset the arrangement of the board. 

Users use the keyboard to input their actions. Each number corresponds to the movement of a piece to a certain position. However, players need not worry about making invalid moves, as the game provides all the possible moves the player could make, requiring the user to pick one of them. Each player takes a turn and the move switches, with white moving first. After each move, the console displays the board with the current arrangement of pieces.

## Stages of Development

The building blocks of the game was the class Square. It has data members such as the piece, rank and file and acts as an advanced coordinate map. These squares are stored in a 2D array called Board, and are accessed through speicifc Board indexes. While in chess, files are stored as letters A-H, in this class, they use a dictionary with A corresponding to 1 and so on. Because of the way python indexes arrays, in order to locate a square on the chessboard, the appropriate index would be Board[file -1][rank-1], for example, A1 would be Board[0][0]. The squares get initialized with an empty piece

After the construction of the Board, I had to create pieces. Each piece was a derived class from a parent piece class which contains the barebones such as position, color and certain member functions. From there, each piece had to be coded with its own set of legal moves and legal captures. While the Pawn, Rook, Bishop and Queen are straightforward, Kings and Knights required more conditions as knights can "jump" over pieces and Kings have several conditions to check for such as whether the square it is moving to is under attack by an opposing piece. In order to code King::Check_Legal, I made several edits as implementing an efficient way to check for every condition was a challenge. 

The general move_piece function looked like this (Example of bishop). The print statement was for the debugging process.

```
def move_piece (self, new_pos):
    if self.check_bishop_move(new_pos):
        if new_pos.piece == 0:
            self.move(new_pos)
        else:
            self.capture(new_pos)
    else:
        print ("Error")
```
Another important function was playermove, which checks through all the pieces of the users color that can move, and provides a list. Then, depending on the user's selection provides a list of squares it can move to. However, in the case of the check, the program automatically selects the King and forces the user to move it. 

It makes use of this function, which tells the playermove function whether or not the king is under attack. 

```
def ischeck(self):
    for x in Board:
        for y in x:
            if y.piece != 0:
                if y.piece.check_capture(self.position):
                    return True 
    return False

```
The main function was simple, making use of the implementation of these functions.  

This is the setup of the board, that resets the position of the pieces after every game:

```
Board = [[x for x in ranks] for y in ranks]
    for x in range (8):
        for y in range (8):
            Board[x][y] = Square(x+1,y+1)
```

## Possible Implementation of a GUI


## Authors

* **Subash Sundar Raman** 


