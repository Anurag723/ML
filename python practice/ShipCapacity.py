class ShipCapacity:
    def shipWithinDays(self, weights, days):
        low = 1
        high = sum(weights)
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if self.possible(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def possible(self, weights, days, curr):
        total = 0
        count = 1

        for weight in weights:
            if weight > curr:
                return False

            if total + weight <= curr:
                total += weight
            else:
                count += 1
                total = weight

        return count <= days


if __name__ == "__main__":
    sc = ShipCapacity()
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5

    result = sc.shipWithinDays(weights, days)
    print(f"Minimum ship capacity to ship within {days} days is: {result}")
