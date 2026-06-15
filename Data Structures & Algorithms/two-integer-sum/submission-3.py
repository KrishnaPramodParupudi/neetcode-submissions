class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(0,len(nums)):
            if (target-nums[i]) in diff_dict :
                return [diff_dict.get(target-nums[i]), i]
            else :
                diff_dict[nums[i]] = i
            print(diff_dict)
        
        