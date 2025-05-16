import unittest
from maze import Maze
#(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None)
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    

    def test_maze_create_cells2(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    
    def test_maze_create_cells4(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 14, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    
    def test_reset(self):
        m1 = Maze(0,0, 12,10,14,10)

        for i in range(len(m1._cells)):
            for j in range(len(m1._cells[0])):
                self.assertFalse(m1._cells[i][j].visited)

    


   
    

    
    


if __name__ == "__main__":
    unittest.main()