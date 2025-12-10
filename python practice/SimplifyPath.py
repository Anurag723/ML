class SimplifyPath:
    @staticmethod
    def simplifyPath(path: str) -> str:
        parts = path.split("/")
        stack = []

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


if __name__ == "__main__":
    path1 = "/home/"
    path2 = "/a/./b/../../c/"
    path3 = "/../"
    path4 = "/home//foo/"

    print(SimplifyPath.simplifyPath(path1))  # Output: /home
    print(SimplifyPath.simplifyPath(path2))  # Output: /c
    print(SimplifyPath.simplifyPath(path3))  # Output: /
    print(SimplifyPath.simplifyPath(path4))  # Output: /home/foo
