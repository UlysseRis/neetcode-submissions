class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i,temp))
            else:
                while stack and stack[-1][-1] < temp:
                    inter = stack.pop()
                    result[inter[0]] = i - inter[0] 

                stack.append((i,temp))
        return result