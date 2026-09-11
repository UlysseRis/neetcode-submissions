class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        res = 0
        left = 0

        for right, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res