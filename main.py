from window import Window 
from maze import Maze

def redraw_and_solve(win):
    maze = Maze(100, 50, 10, 10, 50, 50, win)
    maze.solve()

def main():
    win = Window(800, 600, redraw_and_solve_callback=redraw_and_solve)
    redraw_and_solve(win)  
    win.wait_for_close()


if __name__ == "__main__":
    main()
