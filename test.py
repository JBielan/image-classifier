with open('dognames.txt', "r") as infile:
    content = infile.readlines()
    for i in range(len(content)-1):
        content[i] = content[i].strip()
    print(type(content))
    print(content)
