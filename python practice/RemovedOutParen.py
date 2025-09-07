class RemoveOutParan:
    def remove_outer_parentheses(self, s: str) -> str:
        count = 0
        result = []
        
        for char in s:
            if count == 0 and char == '(':
                count += 1
            elif count == 1 and char == ')':
                count -= 1
            elif count > 0 and char == '(':
                result.append(char)
                count += 1
            else:
                result.append(char)
                count -= 1
        
        return ''.join(result)


def main():
    remove_out_paran = RemoveOutParan()

    # Test cases
    s1 = "(()())(())"
    s2 = "()(())"
    s3 = "(()(()))"
    
    # Testing the remove_outer_parentheses method
    print(f"Input: {s1} -> Output: {remove_out_paran.remove_outer_parentheses(s1)}")
    print(f"Input: {s2} -> Output: {remove_out_paran.remove_outer_parentheses(s2)}")
    print(f"Input: {s3} -> Output: {remove_out_paran.remove_outer_parentheses(s3)}")


if __name__ == "__main__":
    main()
