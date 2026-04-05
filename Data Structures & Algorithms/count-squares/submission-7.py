class CountSquares:

    def __init__(self):
        self.arr = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.arr[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for y1 in self.arr[x]:
            side = y1 - y
            if side == 0:
                continue
            
            x3 = x + side
            x4 = x - side

            res += self.arr[x][y1] *  self.arr[x3][y1] * self.arr[x3][y]

            res += self.arr[x][y1] *  self.arr[x4][y1] * self.arr[x4][y]
        
        return res

