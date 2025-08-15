from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        count = defaultdict(int)
        res = []
        n = len(nums)

        # Count frequencies
        for num in nums:
            count[num] += 1

        # Collect elements appearing more than n/3 times
        for key, val in count.items():
            if val > n // 3:
                res.append(key)

        return res

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3, 2, 2, 1, 1]
    result = solution.majorityElement(nums)
    print("Majority elements (> n/3 times):", result)
