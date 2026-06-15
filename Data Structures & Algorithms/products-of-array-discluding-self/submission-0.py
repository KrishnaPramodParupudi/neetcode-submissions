class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_fix = [nums[0]]
        nums_reverse = nums[::-1]
        post_fix = [nums_reverse[0]]
        for i in range(1,len(nums)) :
            pre_fix.append(pre_fix[i-1]*nums[i])
            post_fix.append(post_fix[i-1]*nums_reverse[i])
        post_fix.reverse()
        fin_list = []
        for i in range(0, len(nums)) :
            if i-1 < 0 :
                fin_list.append(post_fix[i+1])
            elif i+1 >= len(nums) :
                fin_list.append(pre_fix[i-1])
            else :
                fin_list.append(pre_fix[i-1]*post_fix[i+1])
        return fin_list
        
        
            


            
            
        