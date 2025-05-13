from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
class Cell():


    def __init__(self, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True, x1 = None, y1 = None, x2 = None, y2 = None, win = None):


        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        
         
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2 
        self.__win = win


    
    def draw(self, canvas: Canvas, fill_color: str):

        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            line.draw(canvas, fill_color)
        
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            line.draw(canvas, fill_color)

        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            line.draw(canvas, fill_color)
        

        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            line.draw(canvas, fill_color)


     





        
        





