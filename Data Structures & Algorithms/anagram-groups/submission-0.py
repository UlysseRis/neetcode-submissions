class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            key = "".join(sorted(s))
            d[key] = d.get(key, []) + [s]
        return list(d.values())