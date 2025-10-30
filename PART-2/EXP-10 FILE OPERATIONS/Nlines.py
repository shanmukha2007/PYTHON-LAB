with open("product.txt", "w") as F:
    F.write("contact:8309417625")
    F.write("shanmukhaprasad7@gmail.com")
    F.close()

def display_first_n(filename, n):
    with open(filename, "r") as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line.strip())
            
display_first_n("product.txt", 5)
