# WAF to check if a string is palindrome or not.
def check_pal(str):
    if str == str[::-1]:
        print("String is palllindrome")
    else:
        print("String is not palindrome")

check_pal("Harsh")
