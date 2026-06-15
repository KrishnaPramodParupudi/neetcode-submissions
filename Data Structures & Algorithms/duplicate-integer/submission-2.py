class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Approach 1 -> HashSet
        #updated_set = set(nums)
        #if len(updated_set) == len(nums) :
         #   return False
        #return True
        
        #Approach 2 -> Sorting
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] :
                return True
        return False

        