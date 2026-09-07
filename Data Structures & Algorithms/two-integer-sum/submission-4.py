class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashy:
                return [hashy[diff], i]
            hashy[num] = i