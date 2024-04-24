myStr = input("Enter myString: ")
# myStr = "heillo woirld"
myStrLower = myStr.lower()
locations = []

for i in range(len(myStrLower)):
    if myStrLower[i] == 'i':
        locations.append(i)


print(locations)