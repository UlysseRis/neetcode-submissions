class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n == m:
            s_dict = {}
            t_dict = {}
            for i in range(n):
                s_dict[s[i]] = s_dict.get(s[i],0) + 1
                t_dict[t[i]] = t_dict.get(t[i],0) + 1
            for key in s_dict:
                if s_dict.get(key, 0) != t_dict.get(key, 0):
                    return False
            return True
        else:
            return False

        