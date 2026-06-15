class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Approach 1 
        # Time and space complexity O(N) 
        #size = len(nums)
        #for i in range(size):
         #   nums.append(nums[i])
        #return nums

        #Approach 2
        #return nums*2

        #Approach 3
        return nums + nums
        