import re

phone = input("Enter phone number (415-555-4242): ")
pattern = r'^\d{3}-\d{3}-\d{4}$'

if re.match(pattern, phone):
    print("Valid ")
else:
    print("Invalid ")
