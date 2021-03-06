'''
Created on Jun 14, 2017

@author: jwang02
'''
'''
A particular item can be removed from set using methods, discard() and remove().

The only difference between the two is that, while using discard() if the item does not exist in the set, 
it remains unchanged. But remove() will raise an error in such condition.

We can also remove all items from a set using clear().
'''
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# If you uncomment line 38,
# you will get an error.
# Output: KeyError: 2

#my_set.remove(2)

# clear my_set
#Output: set()
my_set.clear()
print(my_set)
