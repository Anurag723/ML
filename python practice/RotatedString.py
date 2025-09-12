class RotatedString:
    def rotate_string(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)


if __name__ == "__main__":
    rs = RotatedString()

    s1 = "abcdef"
    g1 = "defabc"

    s2 = "abcde"
    g2 = "abced"

    print(f'Is "{g1}" rotation of "{s1}"? {rs.rotate_string(s1, g1)}')  # True
    print(f'Is "{g2}" rotation of "{s2}"? {rs.rotate_string(s2, g2)}')  # False
