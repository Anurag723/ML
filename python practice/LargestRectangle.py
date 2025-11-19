def largestRectangleAreaII(self, heights):
        stack = []  
        heights.append(0)  
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        # If the stack is empty or the current bar is taller than the top bar in stack, push it to the stack
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Pop the top element
            top_of_stack = stack.pop()
            # Calculate the area with heights[top_of_stack] as the shortest (or minimum height) bar
            area = heights[top_of_stack] * (index if not stack else index - stack[-1] - 1)
            # Update max_area
            max_area = max(max_area, area)

    # Now, pop the remaining bars from stack and calculate area
    while stack:
        top_of_stack = stack.pop()
        area = heights[top_of_stack] * (index if not stack else index - stack[-1] - 1)
        max_area = max(max_area, area)

    return max_area

# Example usage
heights = [2, 1, 5, 6, 2, 3]
print("Maximum area:", largestRectangleArea(heights))  # Output: 10
