friends = [ 'Ashir', 'Ammar', 'Aslam', 'John', 'Jill']
# print the list of friends
print(friends)
# print the first friend in the list
print(friends[0])
# print the second friend in the list
print(friends[1])

print(friends[1:]) # this will print the list starting from the second friend to the end of the list
print(friends[1:3]) # this will print the list starting from the second friend to the third friend

# we can update the list by adding a new friend to the list

friends[1] = 'Ali' # this will update the second friend in the list to Ali
print(friends) # this will print the updated list of friends