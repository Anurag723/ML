class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If any number is zero
        if num1 == "0" or num2 == "0":
            return "0"
        
        n, m = len(num1), len(num2)
        result = [0] * (n + m)
        
        # Reverse iterate like manual multiplication
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1
                
                # Add to the current slot and propagate carry
                s = mul + result[pos2]
                result[pos2] = s % 10
                result[pos1] += s // 10
        
        # Strip leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        
        # Convert to string
        return ''.join(map(str, result[start:]))

class solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))

print(Solution().multiply("5","3"))
print(solution().multiply("5","3"))