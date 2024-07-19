with open('data.txt', mode="r+") as file:
    file.write("hello and welcome back")

with open('data.txt', mode="r+") as file:
    content = file.read()

print("Text read from the file:",content)
