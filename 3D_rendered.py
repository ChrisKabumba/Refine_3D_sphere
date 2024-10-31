import curses
import math
import time

def draw_sphere(stdscr, x, y, radius):
    for angle in range(0, 360, 5):  # Finer angle for smoother circle
        radians = math.radians(angle)
        sphere_x = int(radius * math.cos(radians)) + x
        sphere_y = int(radius * math.sin(radians) / 2) + y
        if 0 <= sphere_x < curses.COLS and 0 <= sphere_y < curses.LINES:
            stdscr.addch(sphere_y, sphere_x, 'o')

def init_colors():
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

def draw_background(stdscr):
    for y in range(curses.LINES):
        for x in range(curses.COLS):
            if (x + y) % 3 == 0:
                stdscr.addch(y, x, '.')

def move_sphere(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    x, y = curses.COLS // 2, curses.LINES // 2
    radius = 5
    direction_x, direction_y = 1, 1
    speed = 1

    init_colors()

    while True:
        stdscr.clear()
        draw_background(stdscr)  # Draw background
        stdscr.attron(curses.color_pair(1))
        draw_sphere(stdscr, x, y, radius)
        stdscr.attroff(curses.color_pair(1))

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('+') and radius < 15:
            radius += 1  # Increase radius
        elif key == ord('-') and radius > 1:
            radius -= 1  # Decrease radius
        elif key == ord('r'):
            radius = 5  # Reset radius

        # Boundary detection
        if x + radius >= curses.COLS - 1 or x - radius <= 0:
            direction_x *= -1
        if y + radius >= curses.LINES - 1 or y - radius <= 0:
            direction_y *= -1

        x += direction_x * speed
        y += direction_y * speed

        stdscr.refresh()
        time.sleep(0.05)

if __name__ == "__main__":
    curses.wrapper(move_sphere)
