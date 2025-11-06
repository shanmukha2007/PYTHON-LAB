class Palindrome:
    def check(self, value):
        str_val = str(value)
        return str_val == str_val[::-1]
    
class WordPalindrome(Palindrome):
    pass
class NumberPalindrome(Palindrome):
    pass

# Example

print("Word:", WordPalindrome().check("madam"))
print("Number:", NumberPalindrome().check(121))
print("Date:", Palindrome().check("20200202"))
