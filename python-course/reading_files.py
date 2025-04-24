employee_file = open("employees.txt", "r")
# Opens the file in read mode
print(employee_file.readable())
# Checks if the file is readable
print(employee_file.read())
# Reads the entire file content
print(employee_file.readline())
# Reads the first line of the file
print(employee_file.readline())
# Reads the second line of the file
print(employee_file.readline())
# Reads the third line of the file
print(employee_file.readlines())
# Reads all lines of the file into a list
for employee in employee_file.readlines():
    print (employee)
# Iterates through each line in the file and prints it
employee_file.close()
# Closes the file after reading
