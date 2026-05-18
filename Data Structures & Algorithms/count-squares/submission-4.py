class CountSquares:

    def __init__(self):
        self.map = defaultdict(int)
        self.points = []
    def add(self, point: List[int]) -> None:
        self.map[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point

        for x,y in self.points:
            if (abs(px-x) != abs(py-y)) or x == px or y == py:
                continue
            res += self.map[(px,y)] * self.map[(x,py)]
        return res