from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(
        10,
        10,
        25,
        25,
        10,
        10,
        win,
    )

    win.wait_for_close()

if __name__ == "__main__":
    main()