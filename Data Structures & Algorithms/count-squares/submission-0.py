class CountSquares:

    def __init__(self):
        self.map = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.map[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point
        for x,y in self.pts:
            if (abs(py-y)!= abs(px-x)) or x == px or py == y:
                continue
            res += self.map[(x,py)] * self.map[(px,y)]
        return res
        
