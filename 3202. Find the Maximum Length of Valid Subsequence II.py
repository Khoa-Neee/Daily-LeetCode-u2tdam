class Solution:
    #khong hieu
    def maximumLength(self, nums, k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
        return res

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 2
    solution = Solution()
    print(solution.maximumLength(nums, k))  # Example usage