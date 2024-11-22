from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    p1 = Point(10, 20)
    p2 = Point(100, 200)
    line = Line(p1, p2)
    win.draw_line(line, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()