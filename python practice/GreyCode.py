class GrayCode:
    def grayCode1(self, n: int):        #Optimal
        result = []
        for i in range(1 << n):
            result.append(i ^ (i >> 1))
        return result
    

    def gray_code(self, n):
        result = []
        size = 1 << n  # 2^n

        for i in range(size):
            result.append(i ^ (i >> 1))  # Gray code formula

        return result


if __name__ == "__main__":
    gc = GrayCode()

    n = 3  # you can change this value

    gray_codes = gc.gray_code(n)

    print(f"Gray Code for n = {n}:")
    for code in gray_codes:
        print(code)
