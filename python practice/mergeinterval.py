class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if(len(intervals)<=1): return intervals

        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            end = res[-1]
            si = intervals[i]

            if(end[1]>=si[0]):
                end[1] = max(si[1], end[1])

            else:
                res.append(si)

        return res
    
s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
