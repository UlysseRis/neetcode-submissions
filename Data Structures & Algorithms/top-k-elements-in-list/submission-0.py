class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = {}
        for n in nums:
            dico[n] = dico.get(n, 0) + 1
        top_k = sorted(dico, key=dico.get, reverse=True)[:k]
        return top_k
        