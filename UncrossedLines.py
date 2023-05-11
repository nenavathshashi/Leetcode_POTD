class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(dp, pre, ind) :
            if ind==n or pre>=m:
                return 0
            if dp[ind][pre]!=-1:
                return dp[ind][pre]
            ans=helper(dp, pre, ind+1) 
            for i in range(pre, m) :
                if nums1[ind]==nums2[i]:
                    ans=max(ans, 1+helper(dp, i+1, ind+1)) 
            dp[ind][pre]=ans
            return dp[ind][pre]
        n=len(nums1) 
        m=len(nums2) 
        dp=[[-1 for _ in range(m) ] for _ in range(n) ]
        return helper(dp, 0,0) 
                    