octal_number = input("Enter an octal reading:")

# Convert octal to decimal, then to hexadecimal
decimal_value = int(octal_number, 8)
hex_value = hex(decimal_value)[2:].upper()
print("Octal:", octal_number)
print("Hexadecimal:", hex_value)
