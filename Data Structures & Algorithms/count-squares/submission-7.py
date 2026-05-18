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
            if (abs(x - px) != abs(py-y)) or x == px or py == y:
                continue
            res += self.map[(x,py)] * self.map[(px,y)]
        return res