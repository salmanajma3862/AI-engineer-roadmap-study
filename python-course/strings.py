# strings are the plain text
print("Hello World") # this is a string
# we can change the line of text by adding \n and then text after \n will be printed in the next line
print("Hello\nWorld") # text after \n will be printed in the next line

# lets store the string in a variable

phrase = "Hello World"
# lets print the hello world using the variable
print(phrase) # this will print the string stored in the variable

# Concatenation
# cancatination is the process of joining two or more strings together

# lets concatenate the string with another string

print (phrase + " My name is Salman") # this will print the string stored in the variable and then concatenate it with the string " My name is Salman"
# lets store my name in a variable and use the variable in the concatenation
my_name = "Salman"
print (phrase + " My name is " + my_name) # this will print the string stored in the variable and then concatenate it with the string " My name is Salman"

# lets work with functions
print(phrase.lower()) # this will print the string in lower case

print(phrase.upper()) # this will print the string in upper case

print(phrase.isupper()) # this will print True if the string is in upper case and False if the string is not in upper case

print(phrase.islower()) # this will print True if the string is in lower case and False if the string is not in lower case

print(phrase.upper().isupper()) # this will print True if the string is in upper case and False if the string is not in upper case

print(phrase.lower().islower()) # this will print True if the string is in lower case and False if the string is not in lower case

print(phrase[0]) # this will print the first character of the string
print(phrase[1]) # this will print the second character of the string


