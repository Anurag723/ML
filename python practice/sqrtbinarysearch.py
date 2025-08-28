def floor_sqrt(n):
    si = 1
    ei = n
    res = 1

    while si <= ei:
        mid = si + (ei - si) // 2
        if mid * mid <= n:
            res = mid
            si = mid + 1
        else:
            ei = mid - 1

    return res

if __name__ == "__main__":
    n = 11
    print(floor_sqrt(n))
