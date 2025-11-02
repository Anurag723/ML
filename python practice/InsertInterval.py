from typing import List

class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []

        # Step 1: Add intervals that come before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # Step 3: Add merged interval
        res.append(newInterval)

        # Step 4: Add remaining intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res


# ✅ Example usage
if __name__ == "__main__":
    obj = InsertInterval()
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    result = obj.insert(intervals, newInterval)
    print("Merged Intervals:", result)
