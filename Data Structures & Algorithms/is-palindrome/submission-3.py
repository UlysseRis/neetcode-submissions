class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(c for c in s if c.isalnum())
        return word.lower() == word[::-1].lower()