class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = sorted(nums)
        n = len(l)
        index = 0
        if n == 0:
            return 0
        max_length = 1
        count = 1
        while index < n-1:
            inter = l[index+1] - l[index]
            if inter == 1:
                index +=1
                count +=1
            elif inter == 0:
                index +=1
            else:
                index +=1
                count = 1
            max_length = max(count, max_length)
        return max_length
