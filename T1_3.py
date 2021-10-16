#Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        a=[]
        candies1=[]
        for i in range(0,len(candies)):
            candies1.append(candies[i]+extraCandies)
            if candies1[i]>=max(candies):
                a.append(True)
            else:
                a.append(False)
        return a  
