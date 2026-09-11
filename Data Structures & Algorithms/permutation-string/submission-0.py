class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        freq = Counter(s1)
        res = False
        n = len(s1)
        for right, char in enumerate(s2):
            freq[char] = freq.get(char, 0) - 1
            while freq[char] < 0:
                freq[s2[left]] += 1
                left += 1
            res = res or (right - left + 1 == n)
        return res
        