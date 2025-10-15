from typing import List

class CombinationSumIII:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self._backtrack(1, [], ans, k, n)
        return ans

    def _backtrack(self, start: int, temp: List[int], ans: List[List[int]], k: int, target: int):
        if len(temp) == k and target == 0:
            ans.append(temp[:])  # Make a copy of temp
            return
        if len(temp) > k or target < 0:
            return

        for i in range(start, 10):
            temp.append(i)
            self._backtrack(i + 1, temp, ans, k, target - i)
            temp.pop()

# Run the code
if __name__ == "__main__":
    obj = CombinationSumIII()
    k = 3
    n = 7
    result = obj.combinationSum3(k, n)
    print(f"Combinations for k = {k}, n = {n}:")
    for combo in result:
        print(combo)
