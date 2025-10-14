from typing import List

class SubsetII:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self._backtrack(0, [], result, nums)
        return result

    def _backtrack(self, start: int, temp: List[int], result: List[List[int]], nums: List[int]):
        result.append(temp[:])  # Add a copy of the current subset

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            temp.append(nums[i])
            self._backtrack(i + 1, temp, result, nums)
            temp.pop()  # Backtrack

# Runner code
if __name__ == "__main__":
    subset_generator = SubsetII()
    nums = [1, 2, 2]  # Example input
    result = subset_generator.subsetsWithDup(nums)

    print("Unique subsets:")
    for subset in result:
        print(subset)
