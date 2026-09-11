class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)


        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                curr_i,_ = stack.pop()
                answer[curr_i] = i - curr_i

            stack.append((i,t))
        
        return answer