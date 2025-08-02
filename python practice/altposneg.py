class Solution:
    @staticmethod
    def rearrangeArray(nums: list) -> list:
        res = [0] * len(nums)
        even, odd = 0, 1

        for num in nums:
            if num >= 0:
                res[even] = num
                even += 2
            else:
                res[odd] = num
                odd += 2

        return res

def main():
    sol = Solution()
    nums = [3, 1, -2, -5, 2, -4]
    result = sol.rearrangeArray(nums)
    print(result)

if __name__ == "__main__":
    main()
