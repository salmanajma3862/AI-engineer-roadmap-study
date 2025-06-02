# collection or data structures, you can call it a "variable" in which we can save more than one values
# list = [] ordered and changeable, duplicates OK
# set = {} unordered and immutables, no duplicates, but can add/remove
# tuples = () ordered and immutable, duplicate OK. FASTER
# dictionary = () is a collection of key: value pairs

# list
# list can be created using literal syntax [] or list() constructor

#fruits = ["apple", "banana", "orange", "pineapple"]
#or
# fruits = list (("apple", "banana", "orange", "pineapple")) # from a tuple
# list methods
# indexing

#print(fruits[0]) # -> apple (first item in list)
#print(fruits[1]) # -> banana (second item in list)

# negative indexing

#print(fruits[-1]) # -> pineapple (first item but from last)

# slicing

#print(fruits[1:3]) # will print 2nd and 3rd item in list (1 is inclusive and 3 is exclusive, so will not print 3rd index item)
#print(fruits[:2]) # will print upto 2 index items (2 is exclusive)
#fruits.append("apple") # will add apple in the last
#fruits.clear() # will clear the list
# print(fruits.count("banana")) # will count the number of banana in list
# print(fruits.index("orange")) # will print the index/position in list
#fruits.insert(0, "apple") # will add apple at index position 0 in list
#fruits.sort() # sort the list in ascending order -> ['apple', 'banana', 'orange', 'pineapple']
#fruits.reverse() # sort the list in descending order -> ['pineapple', 'orange', 'banana', 'apple']
#print(fruits)
#fruits.remove("banana") # removes first banana element from element
#print(fruits)
#print(fruits.pop()) # removes and return element at given index (default last)
#print(fruits.pop(1)) # will return 2nd element in list

#print(fruits)


# concatenation 

# concatenation = list1 + list2

#membership

# 'apple' in fruits # True or False 

# length

# len(fruits) # total number of fruits in fruits list

# iteration

# for item in fruits # iterates every fruit in fruits list

# built in functions

sum([1, 2, 3]) # 6
min([1, 2, 3]) # 1
max([1, 2, 3]) # 3

'''----------------------'''

# set

# set is created using {} or set()

empty_set = set()
primes = {2, 3, 5, 7, 11}
mixed = {1, "apple", 12.0}
# empty set is created using set(), {} creates empty dictionary

# Accessing and Membership

# sets are unordered so no indexing or slicing

# membership test: x in s returns True or False
# 3 in primes returns True
# 4 in primes returns False

# common set methods

#primes.add(4) # adds 4 to the set
#print(primes)
primes.update([17, 19], {23, 29}) # add multiple elements
primes.discard(29) # remove an element if present
primes.pop()  # removes any arbitarary element from set
primes.copy() # copy entire set
primes.clear() # clear the set
#print(primes)


# tuples
# tuples are immutable, ordered collection of items

fruits_tuple = ("apple", "banana", "orange", "pineapple")

#print(fruits_tuple.index("banana"))  # returns index of banana in tuple
#print(fruits_tuple.count("apple"))  # returns count of apple in tuple


# Dictionary
# dictionary is a collection of key-value pairs, unordered, mutable, and indexed
# created using {} or dict() constructor

country_capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "Germany": "Berlin",
                    "Pakistan": "Islamabad"}

# Dictionary methods

# get method
#print(country_capitals.get("Pakistan"))

#update method
country_capitals.update({"China": "Beijing"})
#update an existing key value pair
country_capitals.update({"Pakistan": "Karachi"})

# pop method -> it removes a value from dictionary
country_capitals.pop("China")
# popitem method -> removes the latest key value pair from dictionary
country_capitals.popitem()

# clear method -> clears the complete dictionary

country_capitals.clear()
print(country_capitals)