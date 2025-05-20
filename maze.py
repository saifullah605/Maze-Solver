from cell import Cell
import time
import random
class Maze():

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
       

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self.__reset_cells_visited()
    
    
    def _create_cells(self):
        self._cells = []
        
        for i in range(self.__num_cols):
            row = []

            for j in range(self.__num_rows):
                
                row.append(Cell(self.__win))
            
            self._cells.append(row)
        
        if self.__win is None:
            return
        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):

        if self.__win is None:
            return
    
        cell_pos_x = self.__cell_size_x*i + self.__x1
        cell_pos_y = self.__cell_size_y*j + self.__y1

        self._cells[i][j].draw(cell_pos_x,cell_pos_y, cell_pos_x+self.__cell_size_x, cell_pos_y+self.__cell_size_y)

        self._animate()

    
    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.03)
    

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.__num_cols-1][self.__num_rows-1]

        entrance_cell.has_left_wall = False
        exit_cell.has_right_wall = False

        self._draw_cell(0,0)
        self._draw_cell(self.__num_cols-1,self.__num_rows-1)
    

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True

        while(True):
            to_visit = []
            #right or left
            if i+1 < self.__num_cols:
                if not self._cells[i+1][j].visited:
                    to_visit.append(("right", i+1, j ))
            
            if i-1 >= 0 :
                if not self._cells[i-1][j].visited:
                    to_visit.append(("left", i-1, j))

            
            #bottom or top

            if j+1 < self.__num_rows:
                if not self._cells[i][j+1].visited:
                    to_visit.append(("bottom", i, j+1 ))
            
            if j-1 >= 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append(("top", i, j-1))
            

            if len(to_visit) == 0:
                
                return


            direction = random.choice(to_visit)

            if direction[0] == "bottom":


                self._cells[i][j].has_bottom_wall = False
                self._cells[direction[1]][direction[2]].has_top_wall = False
                
            
            elif direction[0] == "top":
                self._cells[i][j].has_top_wall = False
                self._cells[direction[1]][direction[2]].has_bottom_wall = False
                
            

            elif direction[0] == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[direction[1]][direction[2]].has_left_wall = False
                
            
            elif direction[0] == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[direction[1]][direction[2]].has_right_wall = False
            

       
                
            self._draw_cell(i,j)
            self._draw_cell(direction[1], direction[2])

            self._break_walls_r(direction[1],direction[2])
        
    
    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j].visited = False
    

    def solve(self):
        return self._solve_r(0,0)

    
    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True
        if i == self.__num_cols-1 and j == self.__num_rows-1:
            return True

        #left
        if i > 0 and not self._cells[i-1][j].visited and  not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        
        #right
        if i < self.__num_cols-1 and not self._cells[i+1][j].visited and  not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        
        #down
        if j < self.__num_rows-1 and not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        
        #Top
        if j > 0  and not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        

        return False


    

        #if not self._cells[i][j].has_top_wall and self._cells[]





    

   
