class JumpGameII:
    def jump(self, nums):
        jump = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jump += 1
                end = farthest

        return jump


def main():
    solution = JumpGameII()

    nums1 = [2, 3, 1, 1, 4]
    nums2 = [2, 3, 0, 1, 4]
    nums3 = [1, 2, 1, 1, 1]

    print(f"Minimum jumps for [2,3,1,1,4]: {solution.jump(nums1)}")  # Expected: 2
    print(f"Minimum jumps for [2,3,0,1,4]: {solution.jump(nums2)}")  # Expected: 2
    print(f"Minimum jumps for [1,2,1,1,1]: {solution.jump(nums3)}")  # Expected: 3


if __name__ == "__main__":
    main()
