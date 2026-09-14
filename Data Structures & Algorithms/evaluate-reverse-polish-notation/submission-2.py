class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                right = stack.pop()
                left = stack.pop()

                if char == "+":
                    res =  left + right
                elif char == "-":
                    res =  left - right
                elif char == "*":
                    res =  left * right
                elif char == "/":
                    res =  int(left/right)

                stack.append(int(res))
        
        return stack[-1]