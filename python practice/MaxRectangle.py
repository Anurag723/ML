from typing import List

class MaxRectangle:

    @staticmethod
    def maximalRectangle(matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, MaxRectangle.largestRectangleArea(heights))

        return max_area

    @staticmethod
    def largestRectangleArea(height: List[int]) -> int:
        n = len(height)
        leftLowest = [-1] * n
        rightLowest = [n] * n

        for i in range(1, n):
            p = i - 1
            while p >= 0 and height[p] >= height[i]:
                p = leftLowest[p]
            leftLowest[i] = p

        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and height[p] >= height[i]:
                p = rightLowest[p]
            rightLowest[i] = p

        res = 0
        for i in range(n):
            width = rightLowest[i] - leftLowest[i] - 1
            res = max(res, height[i] * width)

        return res


if __name__ == "__main__":
    matrix = [
        ['1','0','1','0','0'],
        ['1','0','1','1','1'],
        ['1','1','1','1','1'],
        ['1','0','0','1','0']
    ]

    result = MaxRectangle.maximalRectangle(matrix)
    print("Maximal Rectangle =", result)
