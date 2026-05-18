class CountSquares:

    def __init__(self):
        self.map = defaultdict(int)
        
        
    def add(self, point: List[int]) -> None:
        self.map[tuple(point)] += 1
    
    def count(self, point: List[int]) -> int:
        res = 0
        px,py = point
        for (x,y) ,cnt in list(self.map.items()):
            if (abs(x - px) != abs(py-y)) or x == px or py == y:
                continue
            res += cnt * self.map[(x,py)] * self.map[(px,y)]
        return res