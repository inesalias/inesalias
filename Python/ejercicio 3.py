
#Read the data and save it in a list as 'customers'
customers = []

nameFile1 = "C:/Users/inali\Desktop/github/programa 3/geraldine_customers.txt"
nameFile2 = "C:/Users/inali/Desktop/github/programa 3/gerard_customers.txt"
nameFileOut = "C:/Users/inali/Desktop/github\programa 3/merged_customers.txt"


print("I read the file: " + nameFile1)

file1 = open(nameFile1, "r")
for line in file1:
    parts = line.strip().split(",")
    print(line)
    customers.append((int(parts[0]), parts[1], parts[2], parts[3]))
file1.close()

print("I read the file: " + nameFile2)

file2 = open(nameFile2, "r")
for line in file2:
    parts = line.strip().split(",")
    print(line)
    customers.append((int(parts[0]), parts[1], parts[2], parts[3]))
file2.close()

# Sort the “customers” list by customer number (first field)
customers.sort(key=lambda x: x[0])

# Save the result in a new file

print("I write in the file" + nameFileOut)
output = open(nameFileOut, "w")
for cust in customers:
    line = f"{cust[0]},{cust[1]},{cust[2]},{cust[3]}\n"
    output.write(line)
    print(line)
output.close()

print("Combined file created successfully: merged_customers.txt")
