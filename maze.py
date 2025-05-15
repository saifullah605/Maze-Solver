from cell import Cell
import time
class Maze():

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self._create_cells()
    
    
    def _create_cells(self):
        self._cells = []
        
        for i in range(self.__num_cols):
            row = []

            for j in range(self.__num_rows):
                row.append(Cell(self.__win))
            
            self._cells.append(row)
        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        cell_pos_x = self.__cell_size_x*j + self.__x1
        cell_pos_y = self.__cell_size_y*i + self.__y1

        self._cells[i][j].draw(cell_pos_x,cell_pos_y, cell_pos_x+self.__cell_size_x, cell_pos_y+self.__cell_size_y)
        self._animate()

    
    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)



        

        

            
        
