from typing import List

class PermutationII:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to easily skip duplicates
        used = [False] * len(nums)
        self._backtrack(res, [], nums, used)
        return res

    def _backtrack(self, res: List[List[int]], temp: List[int], nums: List[int], used: List[bool]):
        if len(temp) == len(nums):
            res.append(temp[:])  # Append a copy of current permutation
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            temp.append(nums[i])
            self._backtrack(res, temp, nums, used)
            temp.pop()
            used[i] = False


if __name__ == "__main__":
    nums = [1, 1, 2]
    solution = PermutationII()
    result = solution.permuteUnique(nums)

    print("Unique permutations:")
    for perm in result:
        print(perm)
