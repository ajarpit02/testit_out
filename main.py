from math_utils import add, subtract, multiply, divide
from string_utils import reverse_string, count_words, is_palindrome

def main():
    print("Math Utils Demo:")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))

    print("\nString Utils Demo:")
    text = "level"
    print("Reverse:", reverse_string(text))
    print("Word Count:", count_words("hello world from github"))
    print("Is Palindrome:", is_palindrome(text))

if __name__ == "__main__":
    main()
