from difflib import SequenceMatcher

product1 = input("Enter first product name: ")
product2 = input("Enter second product name:")

similarity = SequenceMatcher(None, product1, product2).ratio() * 100
print(f"Product Name Similarity: {similarity:.2f}%")
