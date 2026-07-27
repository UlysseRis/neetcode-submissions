class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            d[i] = d.get(i,0) + 1
        sorted_elements = sorted(d, key=d.get, reverse=True)
        return sorted_elements[:k]
        