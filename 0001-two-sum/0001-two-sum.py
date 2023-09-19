class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, n1 in enumerate(nums):
            for idx2, n2 in enumerate(nums):
                if n1+n2 == target and idx1 != idx2:
                    return [idx1, idx2]
