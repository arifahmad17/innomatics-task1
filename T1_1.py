#Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        a=[]
        for i in range(0,len(nums)):
            sum=sum+nums[i]
            a.append(sum)
        return a    
