def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    
    s = "1"
    
    for _ in range(2, n + 1):
        result = []
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1
        
        # Add the last group
        result.append(str(count) + s[-1])
        
        s = "".join(result)
    
    return s


# Example usage:
print(countAndSay(5))  # Output: 111221
