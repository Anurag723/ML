class TrappingRainwater:
    @staticmethod
    def trap(height):
        n = len(height)
        if n == 0:
            return 0

        lftmx = [0] * n
        rgtmx = [0] * n

        # Compute left max for each position
        lftmx[0] = height[0]
        for i in range(1, n):
            lftmx[i] = max(lftmx[i - 1], height[i])

        # Compute right max for each position
        rgtmx[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rgtmx[i] = max(rgtmx[i + 1], height[i])

        # Calculate trapped water
        res = 0
        for i in range(n):
            res += min(lftmx[i], rgtmx[i]) - height[i]

        return res


# Runner (main)
if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    trapped_water = TrappingRainwater.trap(height)
    print("Trapped Rain Water:", trapped_water)
