from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    ans = []
    def sol(start: int, curr: List[int]):
        ans.append(curr[:])  # Make a copy of the current subset
        for i in range(start, len(nums)):
            curr.append(nums[i])
            sol(i + 1, curr)
            curr.pop()  # Backtrack
    
    sol(0, [])
    return ans

# Equivalent of Java's main method
if __name__ == "__main__":
    nums = [1, 2, 3]
    result = subsets(nums)
    for subset in result:
        print(subset)
