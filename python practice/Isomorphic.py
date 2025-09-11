class Isomorphic:
    def is_isomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for sc, tc in zip(s, t):
            if sc in s_to_t:
                if s_to_t[sc] != tc:
                    return False
            else:
                s_to_t[sc] = tc

            if tc in t_to_s:
                if t_to_s[tc] != sc:
                    return False
            else:
                t_to_s[tc] = sc

        return True


# Test cases
if __name__ == "__main__":
    iso = Isomorphic()
    print(iso.is_isomorphic("egg", "add"))     # True
    print(iso.is_isomorphic("foo", "bar"))     # False
    print(iso.is_isomorphic("paper", "title")) # True
    print(iso.is_isomorphic("ab", "aa"))       # False
