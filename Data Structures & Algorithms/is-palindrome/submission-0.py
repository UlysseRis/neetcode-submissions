class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(c.lower() for c in s if c.isalnum())
        n=len(res)
        l=0
        r=n-1
        while l<r:
            if res[l] != res[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        