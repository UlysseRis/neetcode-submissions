class Solution:
    
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
        
    def decode(self, s: str) -> List[str]:
        res = []
        count = 0
        n = len(s)

        while count < n:
            j = s.find("#", count)
            length = int(s[count:j])
            count = j + 1 + length
            res.append(s[j + 1 : count])
        return res


        


