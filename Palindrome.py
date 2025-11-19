def is_palindrome(text: str) -> bool:
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    user_input = input("Enter text: ")
    if is_palindrome(user_input):
        print("True")
    else:
        print("False")