# alphabet_to_decimal.py
def alphabet_to_decimal():
    user_input = input("Enter a string: ")
    for char in user_input:
        print(f"Character: {char} | Decimal: {ord(char)}")

if __name__ == "__main__":
    alphabet_to_decimal()
