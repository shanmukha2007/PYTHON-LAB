with open("data.txt", "w") as F:
    F.write("contact:8309417625")
    F.write("shanmukhaprasad7@gmail.com")
    F.close()
    
def count_python(filename):
    with open(filename, "r") as file:
        text = file.read().lower()
    return text.count("python")

print("Occurrences of 'Python':", count_python("data.txt"))
