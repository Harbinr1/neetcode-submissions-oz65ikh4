class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char not in "(+-/*)":
                stack.append(int(char))
            elif char == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif char == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif char == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif char == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append((int(a / b)))
        return stack[0]