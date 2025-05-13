from window import Window 
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800,600)

    win.draw_cell(Cell(x1=250,y1=250, x2= 300, y2= 300))


    win.wait_for_close()



if __name__ == "__main__":
    main()
