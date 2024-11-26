from cell import Cell
from window import Window
import time
import random

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
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_enterance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self.solve()

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

    def _break_enterance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            if i + 1 < self._num_cols and not self._cells[i+1][j]._visited:
                to_visit.append((i+1,j, "right"))
            if i - 1 >= 0 and not self._cells[i-1][j]._visited:
                to_visit.append((i-1,j, "left"))
            if j + 1 < self._num_rows and not self._cells[i][j+1]._visited:
                to_visit.append((i,j+1, "bottom"))
            if j - 1 >= 0 and not self._cells[i][j-1]._visited:
                to_visit.append((i,j-1, "top"))
            if not to_visit:
                self._draw_cell(i, j)
                return
            chosen = to_visit[random.randrange(len(to_visit))] 
            match chosen[2]:
                case "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[chosen[0]][chosen[1]].has_left_wall = False
                case "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[chosen[0]][chosen[1]].has_right_wall = False
                case "top":
                    self._cells[i][j].has_top_wall = False
                    self._cells[chosen[0]][chosen[1]].has_top_wall = False
                case "bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[chosen[0]][chosen[1]].has_bottom_wall = False
                case _:
                    raise Exception("Invalid direction")
            self._break_walls_r(chosen[0], chosen[1])
        
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False
    
    def solve(self):
       return self._solve_r(0,0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True
        if i == self._num_cols -1 and j == self._num_rows -1:
            return True
        if i + 1 < self._num_cols and not self._cells[i+1][j]._visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        if i - 1 >= 0 and not self._cells[i-1][j]._visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        if j + 1 < self._num_rows and not self._cells[i][j+1]._visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        if j - 1 >= 0 and not self._cells[i][j-1]._visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        return False