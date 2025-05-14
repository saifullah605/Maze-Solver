from window import Window 
from cell import Cell

def main():
    win = Window(800,600)


    cell = Cell(250,250,300,300,win)
    cell2 = Cell(300,250,350,300,win)
    

    cell.draw()
    cell2.draw()

    cell.draw_move(cell2)

    win.wait_for_close()



if __name__ == "__main__":
    main()
