binary_key = input("Enter a binary access key: ")

decimal_key = int(binary_key, 2)

# Simple validity check: key should be even
if decimal_key % 2 == 0:
    print(f"Access Key {binary_key} → Decimal {decimal_key} is VALID ")
else:

    print(f"Access Key {binary_key} → Decimal {decimal_key} is INVALID ")
