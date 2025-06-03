import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10) # No window passed, should use default None
        self.assertEqual(
            len(m1._Maze__cells), # Accessing the name-mangled attribute
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]), # Accessing the first column
            num_rows,
        )

    def test_maze_create_cells_small(self):
        num_cols = 3
        num_rows = 5
        # The x1, y1, cell_size_x, cell_size_y parameters are not critical for this specific test
        # as we are only checking the dimensions of the __cells grid.
        # We pass win=None by not providing the last argument.
        m_small = Maze(0, 0, num_rows, num_cols, 10, 10) 
        
        self.assertEqual(
            len(m_small._Maze__cells), 
            num_cols,
            "Number of columns did not match for small maze." # Optional message
        )
        # We should only check the length of a column if there's at least one column
        if num_cols > 0:
            self.assertEqual(
                len(m_small._Maze__cells[0]), 
                num_rows,
                "Number of rows in the first column did not match for small maze." # Optional message
            )
        elif num_rows == 0 : # If there are no columns, there are no rows in any column
             self.assertEqual(num_rows, 0, "Test setup error: if num_cols is 0, expect num_rows check to reflect that.")

    def test_maze_create_cells_different_dimensions(self):
        num_cols = 7
        num_rows = 15
        m_diff = Maze(50, 50, num_rows, num_cols, 20, 20) # win defaults to None
        
        self.assertEqual(
            len(m_diff._Maze__cells),
            num_cols,
            "Number of columns did not match for different dimensions."
        )
        if num_cols > 0:
            self.assertEqual(
                len(m_diff._Maze__cells[0]),
                num_rows,
                "Number of rows in the first column did not match for different dimensions."
            )

    def test_maze_break_entrance_exit(self):
        # Define some dimensions for the test maze
        num_cols = 10
        num_rows = 12
        
        # Create a Maze instance. 
        # The x1, y1, cell_size_x, cell_size_y values don't matter for this logic test.
        # win will default to None.
        m_test = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Call the method we want to test (using name mangling for "private" method)
        m_test._Maze__break_entrance_and_exit()

        # 1. Check the entrance cell (top-left: column 0, row 0)
        # Ensure the __cells grid is not empty before accessing
        if num_cols > 0 and num_rows > 0:
            entrance_cell = m_test._Maze__cells[0][0]
            self.assertFalse(entrance_cell.has_top_wall, "Entrance cell's top wall should be False.")
            # Optional: Check another wall of the entrance cell to ensure it wasn't accidentally changed
            self.assertTrue(entrance_cell.has_left_wall, "Entrance cell's left wall should still be True.")
        else:
            # If num_cols or num_rows is 0, __break_entrance_and_exit might not be able to operate
            # or this specific assertion isn't relevant.
            # Depending on how your Maze handles 0-size, you might add a different assertion here
            # or ensure the test uses dimensions >= 1. For this test, let's assume num_rows/cols >=1.
            # The problem implies testing with a created maze, so dimensions should be positive.
            pass


        # 2. Check the exit cell (bottom-right: column num_cols-1, row num_rows-1)
        # Ensure the grid is large enough for these indices
        if num_cols > 0 and num_rows > 0: # Or specific checks like num_cols >=1, num_rows >=1
            exit_col_idx = num_cols - 1
            exit_row_idx = num_rows - 1
            exit_cell = m_test._Maze__cells[exit_col_idx][exit_row_idx]
            self.assertFalse(exit_cell.has_bottom_wall, "Exit cell's bottom wall should be False.")
            # Optional: Check another wall of the exit cell
            self.assertTrue(exit_cell.has_right_wall, "Exit cell's right wall should still be True.")
        else:
            pass # Similar to above, handle 0-dimension cases if necessary for your Maze design

    def test_maze_reset_cells_visited(self):
        num_cols = 5
        num_rows = 6
        # Create a Maze instance (win will default to None)
        # When the Maze is created, __init__ will call __break_walls_r and then __reset_cells_visited,
        # so all cells will initially have visited = False.
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        # To specifically test the reset functionality, let's manually set some cells as visited.
        # Ensure the maze has cells before trying to access them.
        if num_cols > 0 and num_rows > 0:
            m._Maze__cells[0][0].visited = True # Manually mark top-left as visited
            if num_cols > 1 and num_rows > 1: # If there's another distinct cell
                m._Maze__cells[1][1].visited = True # Manually mark another cell as visited
        else:
            # This test is more meaningful with a non-empty grid.
            # If testing 0-size mazes, a different assertion might be needed.
            # For now, we assume positive dimensions for this test's purpose.
            self.fail("Test setup error: num_cols and num_rows should be > 0 for this test.")


        # Now, explicitly call the method we are testing
        m._Maze__reset_cells_visited() # Use name mangling for "private" method

        # Assert that all cells now have their 'visited' attribute set to False
        for i in range(num_cols):
            for j in range(num_rows):
                # It's good practice to ensure indices are valid, though range should handle it
                # if __create_cells worked as expected for these num_cols/num_rows.
                self.assertFalse(
                    m._Maze__cells[i][j].visited,
                    f"Cell at column {i}, row {j} should have visited = False after reset, but was True."
                )

if __name__ == "__main__":
    unittest.main()