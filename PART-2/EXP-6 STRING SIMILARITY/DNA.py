from difflib import SequenceMatcher
# Program: DNA Sequence Similarity
dna1 = input("Enter DNA sequence 1: ")
dna2 = input("Enter DNA sequence 2: ")

similarity = SequenceMatcher(None, dna1, dna2).ratio() * 100
print(f"DNA Similarity: {similarity:.2f}%")
