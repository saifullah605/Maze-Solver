from point import Point
from tkinter import Tk, BOTH, Canvas
class Line():

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

        self.x1 = p1.x
        self.y1 = p1.y

        self.x2 = p2.x
        self.y2 = p2.y 

    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line( self.x1, self.y1, self.x2, self.y2, fill = fill_color, width = 2 )
        

