class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_elem = Counter(nums)
        result = [k for k, v in count_elem.most_common(k)]
        return result