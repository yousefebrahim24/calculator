with open('data.txt' , mode="w") as f:
    f.write("hello form the out side")

with open('data.txt' , mode="w") as f:
    file = f.read()
print(f)
