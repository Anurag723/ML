from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i, n = 0, len(words)

        while i < n:
            j, line_length = i, 0

            # 1️⃣ Determine how many words fit in the current line
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            num_words = j - i
            num_spaces = maxWidth - line_length
            line = ""

            # 2️⃣ Handle last line or single-word line (left-justified)
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                # 3️⃣ Fully justify (evenly distribute spaces)
                space_between = num_spaces // (num_words - 1)
                extra_spaces = num_spaces % (num_words - 1)

                for k in range(i, j - 1):
                    line += words[k]
                    spaces_to_add = space_between + (1 if extra_spaces > 0 else 0)
                    line += " " * spaces_to_add
                    if extra_spaces > 0:
                        extra_spaces -= 1
                line += words[j - 1]  # last word in the line

            res.append(line)
            i = j  # move to next line

        return res


# 🔍 Example test
if __name__ == "__main__":
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    for line in sol.fullJustify(words, maxWidth):
        print(f'"{line}"')
