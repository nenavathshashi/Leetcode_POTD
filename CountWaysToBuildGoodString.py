class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD=10**9+7
        def helper(length) :
            if length>high:
                return 0
            if length in dp:
                return dp[length]
            ans=0
            if length>=low:
                ans+=1
            ans+=helper(length+zero) +helper(length+one)
            dp[length]=ans%MOD
            return dp[length]
        dp={}
        return helper(0)
