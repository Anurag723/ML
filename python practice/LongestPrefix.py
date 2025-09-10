from typing import List

class LongestPrefix:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


def main():
    lp = LongestPrefix()

    # Test case 1
    strs1 = ["flower", "flow", "flight"]
    print("Longest Common Prefix:", lp.longest_common_prefix(strs1))  # Output: "fl"

    # Test case 2
    strs2 = ["dog", "racecar", "car"]
    print("Longest Common Prefix:", lp.longest_common_prefix(strs2))  # Output: ""

    # Test case 3
    strs3 = ["interspace", "internet", "internal", "interval"]
    print("Longest Common Prefix:", lp.longest_common_prefix(strs3))  # Output: "inte"

if __name__ == "__main__":
    main()
