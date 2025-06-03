from point import Point
from line import Line

class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if not self.__win:
            return

        
        p1_left = Point(self.__x1, self.__y1)
        p2_left = Point(self.__x1, self.__y2)
        left_wall = Line(p1_left, p2_left)
        if self.has_left_wall:
            self.__win.draw_line(left_wall, "black")
        else: self.__win.draw_line(left_wall, "#fafafa")

        p1_top = Point(self.__x1, self.__y1)
        p2_top = Point(self.__x2, self.__y1)
        top_wall = Line(p1_top, p2_top)
        if self.has_top_wall:
            self.__win.draw_line(top_wall, "black")
        else: self.__win.draw_line(top_wall, "#fafafa")

        p1_right = Point(self.__x2, self.__y1)
        p2_right = Point(self.__x2, self.__y2)
        right_wall = Line(p1_right, p2_right)
        if self.has_right_wall:
            self.__win.draw_line(right_wall, "black")
        else: self.__win.draw_line(right_wall, "#fafafa")

        p1_bottom = Point(self.__x1, self.__y2)
        p2_bottom = Point(self.__x2, self.__y2)
        bottom_wall = Line(p1_bottom, p2_bottom)
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall, "black")
        else: self.__win.draw_line(bottom_wall, "#fafafa")

    def draw_move(self, to_cell, undo=False):
        if not self.__win:
            return

        if undo == False:
            line_color = "red"
        else: 
            line_color = "gray"

        x_center = (self.__x1 + self.__x2) / 2
        y_center = (self.__y1 + self.__y2) / 2
        center_self = Point(x_center, y_center)
        
        x_center_to_cell = (to_cell.__x1 + to_cell.__x2) / 2
        y_center_to_cell = (to_cell.__y1 + to_cell.__y2) / 2
        center_to_cell = Point(x_center_to_cell, y_center_to_cell)

        move = Line(center_self, center_to_cell)
        self.__win.draw_line(move, line_color) 