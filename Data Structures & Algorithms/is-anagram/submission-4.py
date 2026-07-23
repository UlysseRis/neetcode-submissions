class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict(Counter(s))
        d2 = dict(Counter(t))
        return d1 == d2



        