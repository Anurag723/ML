class DistinctSubsequence:
    @staticmethod
    def distinctSubseqII(s: str) -> int:
        res = {}
        DistinctSubsequence.sol(0, [], res, s)
        return len(res)

    @staticmethod
    def sol(start: int, curr: list, res: dict, s: str):
        if len(curr) != 0:
            subseq = ''.join(curr)
            res[subseq] = res.get(subseq, 0) + 1
        
        for i in range(start, len(s)):
            curr.append(s[i])
            DistinctSubsequence.sol(i + 1, curr, res, s)
            curr.pop()

if __name__ == "__main__":
    s = "abc"
    print(DistinctSubsequence.distinctSubseqII(s))
