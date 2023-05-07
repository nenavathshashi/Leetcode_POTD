class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        def binary(val):
            low=0
            high=len(lis)-1
            while(low<=high):
                mid=(low+high)//2
                if lis[mid]<=val:
                    low=mid+1
                elif lis[mid]>val:
                    high=mid-1
                else:
                    return mid+1
            return low
        lis=[obstacles[0]]
        result=[1]
        for val in obstacles[1:]:
            pos=binary(val)
            if pos>len(lis)-1:
                lis.append(val)
                result.append(pos+1)
            else:
                lis[pos]=val
                result.append(pos+1)
        return result
