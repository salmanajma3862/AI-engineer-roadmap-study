# dictionary is a collection of key-value pairs
# dictionary is mutable

monthConversions = { 
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# jan is key and january is value
print(monthConversions["Jan"]) # January
# there is another way to access the value of a key in a dictionary
print(monthConversions.get("Jan")) # January