f = open("info.txt", "a")
f.write("I study in GLA University")
f.close()

#open and read the file after the appending:
f = open("info.txt", "r")
print(f.read())