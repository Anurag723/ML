def reverse_words(s):
    # Split the string by whitespace
    words = s.split()

    # Reverse the list of words and join with a space
    return ' '.join(reversed(words))

# Runner
if __name__ == "__main__":
    input_str = "  Hello   world this   is Python  "
    reversed_str = reverse_words(input_str)

    print("Original: \"" + input_str + "\"")
    print("Reversed: \"" + reversed_str + "\"")
