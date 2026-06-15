class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(reverse=True)

        for i in range(len(cars)):
            pos,speed = cars[i]

            time = (target-pos)/speed

            while not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)        