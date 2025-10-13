from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.backtrack(0, [], ans, candidates, target)
        return ans

    def backtrack(self, start: int, temp: List[int], ans: List[List[int]], candidates: List[int], target: int):
        if target == 0:
            ans.append(list(temp))  # Make a copy
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue  # Skip duplicates
            if candidates[i] > target:
                break

            temp.append(candidates[i])
            self.backtrack(i + 1, temp, ans, candidates, target - candidates[i])
            temp.pop()  # Backtrack


class CombinationII:
    @staticmethod
    def run():
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        solution = Solution()
        result = solution.combinationSum2(candidates, target)
        
        print(f"Combinations that sum to {target}:")
        for comb in result:
            print(comb)


# Run the program
if __name__ == "__main__":
    CombinationII.run()
