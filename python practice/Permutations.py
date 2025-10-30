class Permutations:
    def permute(self, nums):
        res = []
        self._sol(res, [], nums)
        return res

    def _sol(self, res, temp, nums):
        # Base case: if temp has all numbers → add a copy to result
        if len(temp) == len(nums):
            res.append(list(temp))  # make a copy
            return

        # Try each number
        for n in nums:
            if n in temp:
                continue  # skip numbers already used
            temp.append(n)          # choose
            self._sol(res, temp, nums)  # explore recursively
            temp.pop()              # backtrack (undo choice)

def main():
    solution = Permutations()

    nums = [1, 2, 3]
    result = solution.permute(nums)

    print("All permutations of [1, 2, 3]:")
    for perm in result:
        print(perm)

if __name__ == "__main__":
    main()
