class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        MOD=10**9+7
        ans=0
        #using two pointer approach to find the subarry with given condition
        while(left<=right):
            #if subarray is greater than what actuall condition is then decrease the right pointer
            while(left<=right and nums[left]+nums[right]>target):
                right-=1
            if left>right:
                break
            #so this subarray satisifies the condition ,now from all subsets where left is inclusive and right is exclusive
            # [3 5 6] target=9
            # [3]     Subsets
            # [3,5]
            # [3,6]
            # [3,5,6]
            ans+=pow(2,right-left,MOD)
            left+=1
        return ans%MOD
