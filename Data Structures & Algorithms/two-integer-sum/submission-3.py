class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        seen = {}

        for i, val in enumerate(nums):
            complement = target - val

            if complement in seen:
                result[0] = seen[complement]
                result[1] = i
                return result
            else:
                seen[val] = i