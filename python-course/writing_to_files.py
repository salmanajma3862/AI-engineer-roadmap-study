employee_file = open("employees.txt", "r")

# Opens the file in read mode
print(employee_file.read())
# Reads the entire file content

# lets write to the file
employee_file = open("employees.txt", "a")
# Opens the file in append mode
employee_file.write("\nToby - Human Resources")
employee_file.write("\nSam - Software Engineer")

# if we want to write a new file

employee_file = open("employees1.txt", "w")
# Opens the file in write mode
# this will create a new file if it does not exist
# or overwrite the existing file
employee_file.write("\nToby - Human Resources")
employee_file.write("\nSam - Software Engineer")