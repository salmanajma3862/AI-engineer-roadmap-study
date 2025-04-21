friends = [ 'Ashir', 'Ammar', 'Aslam', 'John', 'Jill']
# print the list of friends
print(friends)
# we can extend the list by adding another list to the list
lucky_numbers = [ 4, 8, 15, 16, 23, 42]

# now we will extend the list of friends with the list of lucky numbers
friends.extend(lucky_numbers) # this will add the lucky numbers to the list of friends
print(friends) # this will print the updated list of friends with the lucky numbers

# we can add a new friend to the list by using append function
friends.append('Salman') # this will add Salman to the end of the list
print(friends) # this will print the updated list of friends with Salman at the end of the list

 