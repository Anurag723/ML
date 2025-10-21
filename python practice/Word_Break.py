class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def dfs(subs):
            if subs == "":
                return True
            if subs in memo:
                return memo[subs]

            for i in range(1, len(subs) + 1):
                prefix = subs[:i]
                suffix = subs[i:]

                if prefix in word_set and dfs(suffix):
                    memo[subs] = True
                    return True

            memo[subs] = False
            return False

        return dfs(s)

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]

    solution = Solution()
    result = solution.wordBreak(s, wordDict)
    print("Can be segmented:", result)
