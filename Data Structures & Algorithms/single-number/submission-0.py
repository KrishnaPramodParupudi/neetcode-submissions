class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        expected_sum = sum(nums_set)*2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
        