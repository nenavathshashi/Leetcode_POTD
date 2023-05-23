class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def calcu_score(nums, scores):
            if not nums:
                return 0
            if tuple(nums) in scores:
                return scores[tuple(nums)]
            n = len(nums)/2
            maxscore = 0
            for i in range(int(2*n)):
                for j in range(i+1,int(2*n)):
                    a = nums[i]
                    b=nums[j]
                    nums_copy = nums.copy()
                    #gcd = find_gcd(a,b)
                    nums_copy.remove(a)
                    nums_copy.remove(b)
                    score = int(n*math.gcd(a,b)+calcu_score(nums_copy,scores))
                    if score>maxscore:
                        maxscore=score
            scores[tuple(nums)]=maxscore
            return maxscore
        return calcu_score(nums,{})
