from difflib import SequenceMatcher

essay1 = input( "Enter first essay paragraph:"  )
essay2 = input("Enter second essay paragraph: ")

similarity = SequenceMatcher(None, essay1, essay2).ratio() * 100
print(f"Plagiarism Percentage: {similarity:.2f}%")
