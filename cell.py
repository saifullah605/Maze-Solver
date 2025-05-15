from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
from window import Window
class Cell():


    def __init__(self, win: Window = None):


        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
         
        

        self.__win = win 
    
    def get_center_point(self):
        return Point((self.__x1+self.__x2)/2, (self.__y1 + self.__y2)/2)

       


    
    def draw(self , x1, y1, x2, y2):

        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2 

        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line)
        
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)

        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)
        

        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line)
        

    
    def draw_move(self, to_cell, undo = False):
        color = "red"

        if undo:
            color = "gray"
        
        line = Line(self.get_center_point(), to_cell.get_center_point())
        self.__win.draw_line(line, color)


        