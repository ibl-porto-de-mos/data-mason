# Writing to a file
with open("scriptures.txt", "w") as file:
    file.write("In the beginning, God created the heavens and the earth.\n")
    file.write("For God so loved the world...\n")

# Reading from a file
with open("scriptures.txt", "r") as file:
    content = file.read()
    print(content)