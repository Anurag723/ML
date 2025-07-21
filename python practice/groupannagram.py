from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            # Sort the string and use it as the key
            sorted_str = ''.join(sorted(s))
            res[sorted_str].append(s)
        
        # Return the grouped anagrams
        return list(res.values())

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = solution.groupAnagrams(input_list)
    print(grouped)
