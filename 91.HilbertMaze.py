hilbert_map = {'a': {(0, 0): 'b', (0, 1): 'a', (1, 0): 'd', (1, 1): 'a'},
               'b': {(0, 0): 'a', (0, 1): 'c', (1, 0): 'b', (1, 1): 'b'},
               'c': {(0, 0): 'c', (0, 1): 'b', (1, 0): 'c', (1, 1): 'd'},
               'd': {(0, 0): 'd', (0, 1): 'd', (1, 0): 'a', (1, 1): 'c'}}


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __rshift__(self, n):
        return Point(self.x >> n, self.y >> n)

    def __str__(self):
        return 'Point(%d, %d)' % (self.x, self.y)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return [self.x, self.y][index]


def SmallMaze(n, x, y):
    length = 1 << n
    current_squares = ['a']
    ld_ru = [[Point(0, 0), Point(length << 1, length << 1)]]
    for _ in range(n - 1):
        lowleft, upright = ld_ru[-1]
        mid = (lowleft + upright) >> 1
        quad_x = 1 if x >= mid.x else 0
        quad_y = 1 if y >= mid.y else 0
        current_squares += hilbert_map[current_squares[-1]][(quad_x, quad_y)]
        if not quad_x and not quad_y:
            ld_ru += [[lowleft, mid]]
        elif not quad_x and quad_y:
            ld_ru += [[Point(lowleft.x, mid.y), Point(mid.x, upright.y)]]
        elif quad_x and not quad_y:
            ld_ru += [[Point(mid.x, lowleft.y), Point(upright.x, mid.y)]]
        else:
            ld_ru += [[mid, upright]]
        length >>= 1
    current_squares.reverse()
    ld_ru.reverse()

    return current_squares, ld_ru


def moveout(point, current_square, ldru):
    lowleft, upright = ldru
    if point.x == lowleft.x or point.y == lowleft.y or point.x == upright.x or point.y == upright.y:
        return point
    mid = (lowleft + upright) >> 1
    if current_square == 'a':
        if point.y <= mid.y:
            return Point(mid.x, lowleft.y)
        else:
            return Point(mid.x, upright.y)
    elif current_square == 'b':
        if point.x <= mid.x:
            return Point(lowleft.x, mid.y)
        else:
            return Point(upright.x, mid.y)
    elif current_square == 'c':
        if point.y >= mid.y:
            return Point(mid.x, upright.y)
        else:
            return Point(mid.x, lowleft.y)
    else:
        if point.x >= mid.x:
            return Point(upright.x, mid.y)
        else:
            return Point(lowleft.x, mid.y)


def solution(N, A, B, C, D):
    cs_AB, ld_ru_AB = SmallMaze(N, A, B)
    cs_CD, ld_ru_CD = SmallMaze(N, C, D)
    moveout_AB = [Point(A, B)]
    moveout_CD = [Point(C, D)]
    mazesize = 1 << N + 1
    for i in range(N):
        Point_AB = moveout_AB[-1]
        Point_CD = moveout_CD[-1]
        moveout_AB.append(moveout(Point_AB, cs_AB[i], ld_ru_AB[i]))
        moveout_CD.append(moveout(Point_CD, cs_CD[i], ld_ru_CD[i]))
    common = -1
    for i in range(N + 1):
        if moveout_AB[i] == moveout_CD[i]:
            common = i
            break
    dist = 0
    if common > -1:
        for _ in range(common, N + 1):
            moveout_AB.pop()
            moveout_CD.pop()
        if moveout_AB:
            dist = moveout_AB[-1] - moveout_CD[-1]
    else:
        end_AB = moveout_AB[-1]
        end_CD = moveout_CD[-1]
        minx_AB = min(end_AB.x, mazesize - end_AB.x)
        minx_CD = min(end_CD.x, mazesize - end_CD.x)
        miny_AB = min(end_AB.y, mazesize - end_AB.y)
        miny_CD = min(end_CD.y, mazesize - end_CD.y)
        minx = 2 * min(minx_AB, minx_CD) * (end_AB.y != end_CD.y)
        miny = 2 * min(miny_AB, miny_CD) * (end_AB.x != end_CD.x)
        dist = (moveout_AB[-1] - moveout_CD[-1]) + minx + miny
    cnt = len(moveout_AB)
    for i in range(cnt - 2, -1, -1):
        dist += (moveout_AB[i] - moveout_AB[i + 1]) + \
            (moveout_CD[i] - moveout_CD[i + 1])
    return dist


import timeit
print(timeit.timeit('solution(25, 2, 1, 3, 4)', globals=globals(), number=1))
