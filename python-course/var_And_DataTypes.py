# baisc data types are strings, integers, and booleans
# boolean is a data type that can only be true or false
# example
# is_student = True
# strings are data types that are enclosed in quotes
# example
# name = "John"
# integers are data types that are whole numbers
# example
# age = 30

# print the age without converting to string
character_name = "George" # its a string data Type
character_age = 70 # its a integer data type

print("There was once a man named " + character_name + " ,")
# have to convert the integer to string
print("he was a " + str(character_age) + "years old. ")
print("He really liked the name " + character_name + ", ")
# have to convert the integer to string
print("but he didn't like being " + str(character_age) + " years old.")


# variable can be changed halfway through the code

character_name = "George"
character_age = 70

print("There was once a man named " + character_name + " ,")
#have to convert the integer to string
print("he was a " + str(character_age) + "years old. ")

#variable value can be changed halfway through the code
character_name = "John"

print("He really liked the name " + character_name + ", ")
# have to convert the integer to string
print("but he didn't like being " + str(character_age) + " years old.")

#2. print again but this time using a string variable
character_name = "George"
character_age = "70"

print("There was once a man named " + character_name + " ,")
# no need to convert the integer to string because the variable is already a string
print("he was a " + character_age + "years old. ")
print("George liked the name " + character_name + ", ")
# no need to convert the integer to string because the variable is already a string
print("but he didn't like being " + character_age + " years old.")

