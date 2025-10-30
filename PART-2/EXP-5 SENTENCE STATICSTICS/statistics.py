sentence = input("Enter a sentence: ")

words = sentence.split()
digits = sum(ch.isdigit() for ch in sentence)
uppercase = sum(ch.isupper() for ch in sentence)
lowercase = sum(ch.islower() for ch in sentence)

print("Words:", len(words))
print("Digits:", digits)
print("Uppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
