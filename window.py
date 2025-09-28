from tkinter import Tk, BOTH, Canvas, Button
from line import Line


class Window():
    def __init__(self, width, height, redraw_and_solve_callback=None):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root, bg="white", height = height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

         # Add Redraw & Solve button
        self.redraw_button = Button(self.__root, text="Redraw & Solve", command=self._on_redraw_and_solve)
        self.redraw_button.pack()

        self.redraw_and_solve_callback = redraw_and_solve_callback

        self.__root.protocol("WM_DELETE_WINDOW", self.close)



    def _on_redraw_and_solve(self):
        self.canvas.delete("all")  
        if self.redraw_and_solve_callback:
            self.redraw_and_solve_callback(self)  

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    

    def wait_for_close(self):

        self.running = True

        while(self.running):
            self.redraw()
    
    def close(self):
        self.running = False


    def draw_line(self, line: Line, fill_color = "black"):
        line.draw(self.canvas, fill_color)
    

 






        

        
