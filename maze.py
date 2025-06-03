import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        if seed is not None:
            random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        self.__break_entrance_and_exit()
        

    def __create_cells(self):
        for i in range(self.__num_cols):
            column_cells = []
            for j in range(self.__num_rows):
                cell = Cell(self.__win)
                column_cells.append(cell)
            self.__cells.append(column_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i,j)
    
    def __draw_cell(self, i, j):
        cell_x1_on_canvas = self.__x1 + (i * self.__cell_size_x)
        cell_y1_on_canvas = self.__y1 + (j * self.__cell_size_y)
        cell_x2_on_canvas = cell_x1_on_canvas + self.__cell_size_x
        cell_y2_on_canvas = cell_y1_on_canvas + self.__cell_size_y

        target_cell = self.__cells[i][j]
        target_cell.draw(cell_x1_on_canvas, cell_y1_on_canvas, cell_x2_on_canvas, cell_y2_on_canvas)

        self.__animate()

    def __break_entrance_and_exit(self):
        entrance_cell = self.__cells[0][0]
        entrance_cell.has_top_wall = False
        self.__draw_cell(0, 0)

        exit_cell = self.__cells[self.__num_cols - 1][self.__num_rows - 1] 
        exit_cell.has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, column_index, row_index):
        current_cell = self.__cells[column_index][row_index]
        current_cell.visited = True

        while True:
            unvisited_neighbor_indices = []
            if (row_index - 1) >= 0 and (row_index - 1) < self.__num_rows and column_index >= 0 and column_index < self.__num_cols:
                if self.__cells[column_index][row_index - 1].visited == False:
                    unvisited_neighbor_indices.append((column_index, row_index - 1))
            if (row_index + 1) >= 0 and (row_index + 1) < self.__num_rows and column_index >= 0 and column_index < self.__num_cols:
                if self.__cells[column_index][row_index + 1].visited == False:
                    unvisited_neighbor_indices.append((column_index, row_index + 1))
            if (column_index - 1) >= 0 and (column_index - 1) < self.__num_cols and row_index >= 0 and row_index < self.__num_rows:
                if self.__cells[column_index - 1][row_index].visited == False:
                    unvisited_neighbor_indices.append((column_index - 1, row_index))
            if (column_index + 1) >= 0 and (column_index + 1) < self.__num_cols and row_index >= 0 and row_index < self.__num_rows:
                if self.__cells[column_index + 1][row_index].visited == False:
                    unvisited_neighbor_indices.append((column_index + 1, row_index))

            if not unvisited_neighbor_indices:
                self.__draw_cell(column_index, row_index)
                return
            else:
                chosen_neighbor_coords = random.choice(unvisited_neighbor_indices)
                next_col = chosen_neighbor_coords[0]
                next_row = chosen_neighbor_coords[1]
            
                chosen_neighbor_cell = self.__cells[next_col][next_row]
                if next_col == (column_index + 1) and next_row == row_index:
                    current_cell.has_right_wall = False
                    chosen_neighbor_cell.has_left_wall = False
                elif next_col == (column_index - 1) and next_row == row_index:
                    current_cell.has_left_wall = False
                    chosen_neighbor_cell.has_right_wall = False
                elif next_col == (column_index) and next_row == (row_index - 1):
                    current_cell.has_top_wall = False
                    chosen_neighbor_cell.has_bottom_wall = False
                elif next_col == (column_index) and next_row == (row_index + 1):
                    current_cell.has_bottom_wall = False
                    chosen_neighbor_cell.has_top_wall = False

                self.__break_walls_r(next_col, next_row)

    def __reset_cells_visited(self):
        for column_list in self.__cells:
            for cell in column_list:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, column_index, row_index):
        self.__animate()
        current_cell = self.__cells[column_index][row_index]
        current_cell.visited = True
        if column_index == self.__num_cols - 1 and row_index == self.__num_rows - 1:
            return True
        
        if column_index + 1 < self.__num_cols and row_index >= 0 and row_index < self.__num_rows and current_cell.has_right_wall == False and self.__cells[column_index + 1][row_index].visited == False:
            right_neighbor_cell = self.__cells[column_index + 1][row_index]
            current_cell.draw_move(right_neighbor_cell)
            if self._solve_r(column_index + 1, row_index):
                return True
            else: current_cell.draw_move(right_neighbor_cell, True)

        if (row_index + 1) < self.__num_rows and column_index >= 0 and column_index < self.__num_cols and not current_cell.has_bottom_wall and not self.__cells[column_index][row_index + 1].visited:  
            down_neighbor_cell = self.__cells[column_index][row_index + 1]
            current_cell.draw_move(down_neighbor_cell)
            if self._solve_r(column_index, row_index + 1):
                return True
            else:
                current_cell.draw_move(down_neighbor_cell, True)

        if (column_index - 1) >= 0 and  row_index >= 0 and row_index < self.__num_rows and not current_cell.has_left_wall and not self.__cells[column_index - 1][row_index].visited:
            left_neighbor_cell = self.__cells[column_index - 1][row_index]
            current_cell.draw_move(left_neighbor_cell)
            if self._solve_r(column_index - 1, row_index):
                return True
            else:
                current_cell.draw_move(left_neighbor_cell, True)

        if (row_index - 1) >= 0 and column_index >= 0 and column_index < self.__num_cols and not current_cell.has_top_wall and not self.__cells[column_index][row_index - 1].visited:
            up_neighbor_cell = self.__cells[column_index][row_index - 1]
            current_cell.draw_move(up_neighbor_cell)
            if self._solve_r(column_index, row_index - 1):
                return True
            else:
                current_cell.draw_move(up_neighbor_cell, True)
        
        return False

    def __animate(self):
        if not self.__win:
            return

        self.__win.redraw()
        time.sleep(0.05) 