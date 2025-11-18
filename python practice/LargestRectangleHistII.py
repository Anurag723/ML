class LargestRectangleHistII:

    @staticmethod
    def largestRectangleArea(heights):
        stack = []   # will store indices
        max_area = 0

        for i in range(len(heights)):

            # While current bar is smaller than the bar at top of stack
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]   # height of popped bar

                # If stack empty, left boundary = -1
                left_boundary = stack[-1] if stack else -1

                # width between left_boundary + 1 and i - 1
                width = i - left_boundary - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        # Final cleanup (bars extending to the right end)
        n = len(heights)
        while stack:
            height = heights[stack.pop()]
            left_boundary = stack[-1] if stack else -1
            width = n - left_boundary - 1
            max_area = max(max_area, height * width)

        return max_area


# Simulating "main"
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    result = LargestRectangleHistII.largestRectangleArea(heights)
    print("Largest Rectangle Area =", result)
