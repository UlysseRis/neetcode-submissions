class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1
        while l < n and r>0:
            l_test = numbers[l]
            r_test = numbers[r]
            if r_test + l_test == target and l != r:
                return [l+1, r+1]
            elif r_test + l_test > target:
                r -=1
            else:
                l +=1
        