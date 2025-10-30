def check_phone_format(num):
    if len(num) == 12 and num[3] == '-' and num[7] == '-':
        if num[:3].isdigit() and num[4:7].isdigit() and num[8:].isdigit():
            return True
    return False


phone = input("Enter phone number (415-555-4242): ")

print("Valid" if check_phone_format(phone) else "Invalid")
