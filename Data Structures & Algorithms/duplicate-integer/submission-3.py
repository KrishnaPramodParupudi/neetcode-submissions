class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Approach 1 -> HashSet 
        #space and time -> O(n) extra hashset and iterating n values during set creation
        #updated_set = set(nums)
        #if len(updated_set) == len(nums) :
         #   return False
        #return True
        
        #Approach 2 -> Sorting
        #space and time -> Space is O(1) since list is sorted, Time complexity is O(NlogN) for sorting
        #nums.sort()
        #for i in range(1, len(nums)):
         #   if nums[i] == nums[i-1] :
          #      return True
        #return False

        #Approach 3 -> HashMap
        mymap = {}
        for i in nums:
            if i in mymap:
                return True
            else:
                mymap[i] = i
        return False

        

        