class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Tri en place en C pur
        nums.sort()
        
        max_len = 1
        curr_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                curr_len += 1
            else:
                if curr_len > max_len:
                    max_len = curr_len
                curr_len = 1
                
        return curr_len if curr_len > max_len else max_len