from enum import Enum
class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.color = Color.WHITE    # Used for BFS 0-White, 1-Gray, 2-Black
        self.pi = None              # Used for BFS, represents parent
        self.d = -1                 # Used for BFS, represents distance from starting vertex
    
    def toWhite(self):
        self.color = Color.WHITE
    
    def toGray(self):
        self.color = Color.GRAY
    
    def toBlack(self):
        self.color = Color.BLACK

    def isWhite(self):
        return self.color == Color.WHITE

    def isGray(self):
        return self.color == Color.GRAY
    
    def isBlack(self):
        return self.color == Color.BLACK