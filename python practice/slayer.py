def main():
    print("Guess a six-digit number SLAYER so that following equation is true,")
    print("where each letter stands for the digit in the position shown:")
    print("SLAYER + SLAYER + SLAYER = LAYERS")
    
    slayer = int(input("Enter your guess for SLAYER: "))
    
    # Ensure SLAYER is a six-digit number
    if slayer < 100000 or slayer > 999999:
        print("Your guess is incorrect:")
        print("SLAYER must be a 6-digit number.")
        print("Thanks for playing.")
        return

    # Compute SLAYER + SLAYER + SLAYER
    triple_slayer = 3 * slayer

    # Extract digits of SLAYER
    S = (slayer // 100000) % 10
    L = (slayer // 10000) % 10
    A = (slayer // 1000) % 10
    Y = (slayer // 100) % 10
    E = (slayer // 10) % 10
    R = slayer % 10

    
    layers = (L * 100000 + A * 10000 + Y * 1000 + E * 100 + R * 10 + S)

    if triple_slayer == layers:
        print("Your guess is correct:")
        print(f"SLAYER + SLAYER + SLAYER = {triple_slayer}")
        print(f"LAYERS = {layers}")
    else:
        print("Your guess is incorrect:")
        print(f"SLAYER + SLAYER + SLAYER = {triple_slayer}")
        print(f"LAYERS = {layers}")
    
    print("Thanks for playing.")


main()