class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                l.append(char)
            else:
                if not l:
                    return False
                else:
                    test = l.pop()
                    if test == "(" and char != ")":
                            return False
                    elif test == "{" and char != "}":
                        return False
                    elif test == "[" and char != "]":
                        return False
        if l:
            return False
        return True