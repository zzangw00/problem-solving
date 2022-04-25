BLANK = 0
BLOCK = 1
EXIT = 2
RED = 3
BLUE = 4

n, m = tuple(map(int, input().split()))

red_pos = (0, 0)
blue_pos = (0, 0)
OUT_OF_MAP = (n, m)

ans = 11


def blue_exist():
    return blue_pos != OUT_OF_MAP


def red_exist():
    return red_pos != OUT_OF_MAP


def red_must_first(move_dir):
    (rx, ry), (bx, by) = red_pos, blue_pos

    if move_dir == 0:
        return (ry == by and rx < bx)
    elif move_dir == 1:
        return (ry == by and rx > bx)
    elif move_dir == 2:
        return (rx == bx and ry < by)
    else:
        return (rx == bx and ry > by)


def can_go(x, y):
    return a[x][y] != BLOCK and (x, y) != red_pos and \
                                (x, y) != blue_pos


def get_destination(pos, move_dir):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    curr_x, curr_y = pos
    nx, ny = curr_x + dxs[move_dir], curr_y + dys[move_dir]

    if not can_go(nx, ny):
        return pos

    if a[nx][ny] == EXIT:
        return OUT_OF_MAP

    return get_destination((nx, ny), move_dir)


def tilt(move_dir):
    global red_pos, blue_pos

    if red_must_first(move_dir):
        red_pos = get_destination(red_pos, move_dir)
        blue_pos = get_destination(blue_pos, move_dir)
    else:
        blue_pos = get_destination(blue_pos, move_dir)
        red_pos = get_destination(red_pos, move_dir)


def find_min(cnt):
    global ans, red_pos, blue_pos
    if not blue_exist():
        return
    if not red_exist():
        ans = min(ans, cnt)
        return
    if cnt >= 10:
        return

    for move_dir in range(4):
        temp_red, temp_blue = red_pos, blue_pos
        tilt(move_dir)
        find_min(cnt + 1)
        red_pos, blue_pos = temp_red, temp_blue


def char_to_int(elem):
    if elem == '.':
        return BLANK
    elif elem == '#':
        return BLOCK
    elif elem == 'R':
        return RED
    elif elem == 'B':
        return BLUE
    elif elem == 'O':
        return EXIT


a = [
    list(map(char_to_int, list(input())))
    for _ in range(n)
]
for i in range(n):
    for j in range(m):
        if a[i][j] == RED:
            a[i][j] = BLANK
            red_pos = (i, j)
        if a[i][j] == BLUE:
            a[i][j] = BLANK
            blue_pos = (i, j)
find_min(0)
if ans == 11:
    ans = -1

print(ans)
