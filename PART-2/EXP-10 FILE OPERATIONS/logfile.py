with open("server.log", "w") as F:
    F.write("contact:8309417625")
    F.write("shanmukhaprasad7@gmail.com")
    F.close()
    
def count_error(filename):
    with open(filename, "r") as file:
        text = file.read().lower()
    return text.count("error")

print("Occurrences of 'error':", count_error("server.log"))
