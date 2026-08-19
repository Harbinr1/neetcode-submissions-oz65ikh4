class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] *len(temperatures)

        q = []
        for i,v in enumerate(temperatures):
            while q and v > q[-1][1]:
                prev_i,val = q.pop()
                result[prev_i] = i - prev_i
            q.append((i,v))
        return result




        