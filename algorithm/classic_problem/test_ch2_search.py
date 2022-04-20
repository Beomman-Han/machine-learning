"""Test codes for ch2_search.py module"""

from ch2_search import *

if __name__ == '__main__':
    maze : Maze = Maze()
    print(maze)
    
    print(maze.goal_test(MazeLocation(4, 5)))  ## False
    print(maze.goal_test(MazeLocation(9, 9)))  ## True
    
    print(maze.successors(MazeLocation(0, 0)))