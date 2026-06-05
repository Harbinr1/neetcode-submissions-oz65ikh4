class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort()

        stack = []
        for i in range(len(cars)-1,-1,-1):
            pos,speed = cars[i]
            time = (target - pos) / speed
        

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)