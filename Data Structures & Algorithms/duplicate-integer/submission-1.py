class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        updated_set = set(nums)
        if len(updated_set) == len(nums) :
            return False
        return True
        