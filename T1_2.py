#Shuffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[0:n]
        y=nums[n:2*n]
        a=[]
        for i in range(0,n):
            a.append(x[i])
            a.append(y[i])
        return a  
  
