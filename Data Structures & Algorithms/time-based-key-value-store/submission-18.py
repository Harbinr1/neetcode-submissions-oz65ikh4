from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.storage.get(key,[])
        lo = 0
        hi = len(values) - 1
        latest = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if values[mid][0] == timestamp:
                return self.storage[key][mid][1]
            if values[mid][0] > timestamp:
                hi = mid - 1
            elif values[mid][0] < timestamp:
                latest = mid
                lo = mid + 1
            
        return self.storage[key][latest][1] if latest != -1  else ""
        
