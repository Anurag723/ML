class RomanToInt:
    @staticmethod
    def roman_to_int(s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        rs = 0
        i = 0
        while i < len(s):
            curr = roman_map[s[i]]
            
            # Look ahead to check for subtractive pair
            if i + 1 < len(s):
                next_val = roman_map[s[i + 1]]
                if curr < next_val:
                    rs += next_val - curr
                    i += 2
                    continue
            
            rs += curr
            i += 1
        
        return rs


# Example usage
print(RomanToInt.roman_to_int("MCMXCIV"))  # Output: 1994
