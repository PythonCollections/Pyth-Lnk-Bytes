import re

def checkPalindrome(text):
    text=str(text)
    reversedText=str(text[::-1])

    forwards = ''.join(re.findall(r'[a-z]+',text.lower()))

    if(text == reversedText):
        print("Its Palindrome")
    else:
        print("Its not a palindrome")

if __name__ == "__main__":
    checkPalindrome("go hang a salami, i'm a lasagna hog")
    checkPalindrome("level")