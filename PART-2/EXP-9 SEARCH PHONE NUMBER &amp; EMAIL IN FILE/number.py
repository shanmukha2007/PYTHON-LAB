import re

file = open("contact.txt", "w")
file.write("contact:6309386866")
file.write("shanmukha@gmail.com")
file.close()


def extract_contacts(filename):
    with open(filename, "r") as file:
        text = file.read()

    phones = re.findall(r'\d{10}', text)  # Finds 10-digit phone numbers
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

    return phones, emails


phones, emails = extract_contacts("contact.txt")
print("Phone Numbers:", phones)
print("Emails:", emails)
