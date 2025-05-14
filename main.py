from window import Window 
from cell import Cell

def main():
    win = Window(800,600)


    cell = Cell(win)
    cell2 = Cell(win)
    

    cell.draw(250,250,300,300)
    cell2.draw(300,250,350,300)

    cell.draw_move(cell2)

    win.wait_for_close()



if __name__ == "__main__":
    main()
