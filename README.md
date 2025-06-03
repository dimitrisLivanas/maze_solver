# Maze Solver Project

## Description

This project is a Python application that generates and solves mazes. It uses a randomized Depth-First Search (DFS) algorithm to carve paths through a grid, creating a unique maze each time (or a reproducible one if a seed is provided). The application then employs another DFS algorithm to find and visualize the solution path from a designated entrance to an exit. The entire process, including maze generation and solving, is visualized using Python's Tkinter library.

## Features

* **Maze Generation:** Creates mazes using a randomized Depth-First Search algorithm.
* **Maze Solving:** Finds a path from the entrance (top-left) to the exit (bottom-right) using Depth-First Search.
* **Visualization:** Uses Tkinter to draw the maze, the generation process, and the solving process.
    * Paths explored by the solver are drawn.
    * Backtracking steps during solving are visually distinguished (e.g., different color).
* **Customizable Mazes:** Allows specification of maze dimensions (rows, columns), starting position on the canvas, and cell sizes.
* **Optional Seeding:** Supports providing a seed for the random number generator to produce reproducible mazes, which is useful for debugging and testing.
* **Clear Entrance and Exit:** Automatically creates an entrance at the top-left cell and an exit at the bottom-right cell.
* **Unit Tested:** Includes unit tests for core logic (e.g., maze creation, cell state resets).

## Technologies Used

* Python 3
* Tkinter (for the GUI and drawing canvas)
* `random` module (for maze generation)
* `unittest` module (for testing)

## Setup and Installation

1.  **Python 3:** Ensure you have Python 3.10 or higher installed. You can check your version with:
    ```bash
    python3 --version
    ```
2.  **Tkinter:** Tkinter is usually included with standard Python installations. To check if it's working, run:
    ```bash
    python3 -m tkinter
    ```
    A small window should pop up. If you encounter a `ModuleNotFoundError: No module named '_tkinter'`, you may need to install it separately.
    * **On Debian/Ubuntu-based Linux:**
        ```bash
        sudo apt-get update
        sudo apt-get install python3-tk
        ```
    * **On macOS (using Homebrew):**
        ```bash
        brew install python-tk
        ```
        Ensure your Python installation is correctly linked with this Tk version. You might need to reinstall Python via Homebrew after installing `python-tk`.
    * **On Windows:** Tkinter is typically included with the official Python installer from python.org. Make sure "tcl/tk and IDLE" was selected during installation.

3.  **Project Files:** Clone or download the project files into a local directory. The project includes the following key Python files:
    * `maze_solver.py` - The main application entry point.
    * `maze.py` - Contains the `Maze` class.
    * `cell.py` - Contains the `Cell` class.
    * `window.py` - Contains the `Window` class for Tkinter setup.
    * `point.py` - Contains the `Point` class.
    * `line.py` - Contains the `Line` class.
    * `tests.py` - Contains unit tests.

## How to Run

1.  **To Run the Maze Generator and Solver (Visual Mode):**
    Navigate to the project's root directory in your terminal and run:
    ```bash
    python3 maze_solver.py 
    ```
2.  **To Run Unit Tests:**
    Navigate to the project's root directory and run:
    ```bash
    python3 tests.py
    ```
    This will execute the automated tests and report if they pass or fail.

## Project Structure Overview

* `window.py`: Handles the Tkinter window setup and basic drawing loop.
* `point.py`: Defines a simple Point with x, y coordinates.
* `line.py`: Defines a Line between two Points and can draw itself on a canvas.
* `cell.py`: Represents a single cell in the maze, knowing its walls and how to draw itself and moves to other cells.
* `maze.py`: Contains the main `Maze` logic, including cell grid creation, maze generation algorithm (`__break_walls_r`), entrance/exit creation, and the solving algorithm (`_solve_r`).
* `your_main_script_name.py`: (e.g., `maze_solver.py`) Contains the `main()` function to create a Window and a Maze, and run the application.
* `tests.py`: Unit tests for the project.
* `.gitignore`: Specifies intentionally untracked files that Git should ignore.

---
