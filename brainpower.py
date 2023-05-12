class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def helper(dp,ind) :
            if ind>=n:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            not_take=helper(dp,ind+1) 
            take=questions[ind][0]+helper(dp,ind+questions[ind][1]+1) 
            dp[ind]=max(take, not_take) 
            return dp[ind]
        n=len(questions) 
        dp=[-1 for _ in range(n) ]
        return helper(dp,0)