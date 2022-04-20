"""
This is for practicing contents of searching problem
in Classic Computer Science Problem in Python.
"""

## find path at maze

from enum import Enum
import random
from typing import List, NamedTuple

class Cell(str, Enum):
    """Represent status of each cell in maze"""
    EMPTY   = " "
    BLOCKED = "X"
    START   = "S"
    GOAL    = "G"
    PATH    = "*"


class MazeLocation(NamedTuple):
    """Inherit NamedTuple?
    
    namedtuple example:
    
    from collections import namedtuple
    MazeLocation = namedtuple('MazeLocation', ['row', 'column'])
    """
    
    row : int
    column : int


class Maze:
    def __init__(self,
        rows : int = 10,
        columns : int = 10,
        sparseness : float = 0.2,
        start : MazeLocation = MazeLocation(0, 0),
        goal : MazeLocation = MazeLocation(9, 9)
        ) -> None:
    
        self._rows = rows
        self._columns = columns
        self.start = start
        self.goal = goal
        
        self._grid: List[List[Cell]] = [[Cell.EMPTY for _ in range(columns)]
        for _ in range(rows)]
        
        self._randomly_fill(rows, columns, sparseness)
        
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL
        
        return        
    
    def _randomly_fill(self,
        rows : int,
        columns : int,
        sparseness : float
        ) -> None:
        
        """Fill Cell.BLOCKED at self._grid with some of sparseness"""
        
        for r in range(rows):
            for c in range(columns):
                if random.uniform(0, 1) < sparseness:
                    self._grid[r][c] = Cell.BLOCKED
        
        return
    
    def __str__(self) -> str:
        """Return string format of Maze instance"""
        
        output = ''
        for row in self._grid:
            output += "".join([item.value for item in row]) + '\n'
        return output

    def goal_test(self, loc : MazeLocation) -> bool:
        return loc == self.goal