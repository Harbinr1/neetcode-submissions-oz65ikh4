class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_to_spe = dict(zip(position,speed))
        sorted_position = sorted(position,reverse = True)

        for pos in sorted_position:
            spe = pos_to_spe[pos]
            time = (target - pos) / spe


            if not stack:
                stack.append(time)
            elif time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack) 
        