class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        left = 0
        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(c)
            max_length = max(max_length, right - left + 1)
        return max_length