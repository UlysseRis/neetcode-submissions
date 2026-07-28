class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            i = len(s)
            res = res + str(i) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        n = len(s)
        res = []
        count = 0
        while count < n:
            j = s.find("#", count)
            length = int(s[count:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            count = j + 1 + length
        return res


        


