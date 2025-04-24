#value = 10/0
# This will raise a ZeroDivisionError
try:
    # but if we put it in a try block, we can catch the error
    # but this error will be too broad
    # and we will not know what error it is
    # so we can use specific exceptions
    # for example, we can catch a ZeroDivisionError
    value = 10/0
    #print (value)
    number = int(input("Enter a number: "))
    print (f"The number is {number}")
except ZeroDivisionError as zeroDiv:
    print (zeroDiv)
except ValueError:
    # this will catch a ValueError
    print ("You did not enter a number")