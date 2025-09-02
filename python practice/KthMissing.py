class KthMissing:
    def findKthPositive(self, arr, k):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2
            assumed_missing = arr[mid] - (mid + 1)

            if assumed_missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k


# Driver code to test the function
if __name__ == "__main__":
    obj = KthMissing()

    # Example 1
    arr1 = [2, 3, 4, 7, 11]
    k1 = 5
    print("Output 1:", obj.findKthPositive(arr1, k1))  # Expected: 9

    # Example 2
    arr2 = [1, 2, 3, 4]
    k2 = 2
    print("Output 2:", obj.findKthPositive(arr2, k2))  # Expected: 6

    # Example 3
    arr3 = [5, 6, 8, 9]
    k3 = 4
    print("Output 3:", obj.findKthPositive(arr3, k3))  # Expected: 4
