from cell import Cell
from window import Window
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window= None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._window))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if not self._window:
            return
        x_pos1 = (self._cell_size_x * i) + self._x1
        y_pos1 = (self._cell_size_y * j) + self._y1
        x_pos2 = (self._cell_size_x * (i+1)) + self._x1
        y_pos2 = (self._cell_size_y * (j+1)) + self._y1
        self._cells[i][j].draw(x_pos1, y_pos1, x_pos2, y_pos2)
        self._animate() 

    def _animate(self):
        if not self._window:
            return
        self._window.redraw()
        time.sleep(0.05)