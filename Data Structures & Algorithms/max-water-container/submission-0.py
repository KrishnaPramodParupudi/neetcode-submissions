class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1
        max = 0
        while i<j :
           val = min(heights[j],heights[i]) * (j-i)
           if val > max :
            max = val
           if heights[i] < heights[j] :
            i +=1
           elif heights[i] > heights[j] :
            j -=1
           else :
            i +=1
        return max
        