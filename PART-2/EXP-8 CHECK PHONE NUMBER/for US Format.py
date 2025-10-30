import re

def check_us_phone(num):
    return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', num))

print(check_us_phone("415-555-4242"))  # True
print(check_us_phone("1234567890"))    # False
