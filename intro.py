# python-notes


message = 'Hello World'
message2 = 'Kevin\'s World'
# This works because it "escapes" the single quote"

# message3 = """Bobby's world was a cartoon
# in the 90s"""
# Makes multiple lines

# print('Hello world')
# print(message3)

# print(len(message))

# print(message[0])
# Gets letter at index 0

# print(message[0:5])
# Gets letters 0-4 (Non-inclusive for second number)
# print(message[:5]) would also work
# Conversely, print(message[6:]) also works to get letter 6 to the end

# print(message.count('l'))
# counts how many l's are in the string, returns 3

# message.find('World') prints 6 since it starts at 6th spot

greeting = 'Hello'
name = 'Michael'

message4 = greeting + ' ' + name
message5 = '{}, {}. Welcome!'.format(greeting, name)
# Smoother way of adding strings into strings
message6 = f'{greeting}, {name}. Welcome!'
# This also works
# print(message6)

# print(dir(name))
# Shows all available methods

# print(help(str))
# print(help(str.lower))
# Super useful! explains what methods do for type

num = 1
num += 1
# Increments by 1
num *= 10
# Multiplies by 10

# print(round(3.75))
# Rounds to 4



# LISTS (Mutable)

courses = ['History', 'Math', 'Physics', 'CompSci']

# print(courses)
# print(courses[-1]) # Last item

# print(courses[0:2]) # Grabs within range of two numbers. First index is inclusive, second is not
# print(courses[:2]) # This also works, and vice versa

courses.append('Art') # Adds to end of list
courses.insert(0, 'Chemistry') # Adds to specified index

courses_2 = ['Education', 'English']
courses.extend(courses_2) # Adds the strings from the list to the end of courses
# Useful as appending a list into another will add the list itself and not its contents

# courses.remove('Math')
# print(courses.pop()) # Drops last class from courses, also returns the removed value

# courses.reverse() # Reverses order
# courses.sort() # Sorts in alphabetical order

nums1 = [1, 3474, 3, 56]
nums1.sort() # Sorts in ascending order

# courses.sort(reverse=True) # Sorts in reverse order
nums1.sort(reverse=True) # Sorts in reverse order

sorted_courses = sorted(courses) # returns a sorted courses list. doesn't modify original

# print(courses.index('CompSci')) # Returns index where CompSci is found
# print('Art' in courses) # checks if Art is in courses list and returns true or false

# print(courses)
# print(nums1)

# for index, item in enumerate(courses, start=1):  # Enumerate returns index and value, start=1 will make the list start at 1
    # print(index, item) # Prints index and value

courses_3 = ['History', 'Math', 'Physics', 'CompSci', 'Reading']

course_str = ', '.join(courses) # Adds a comma and space between all courses
new_list = course_str.split(' , ') # does the opposite, returns items into a list

# print(course_str)
# print(new_list)


# TUPLES (Immutable)

# tuple_courses = ('History', 'Math', 'Physics', 'CompSci') 
# created in the same way only using parentheses instead of brackets

# very similar to lists, but cannot be mutated. can be useful if you do not want to accidently change something
# less error prone, also take up less memory


# SETS

set_courses = {'History', 'Math', 'Physics', 'CompSci'}
# Sets do not care about order, good at checking for duplicates and whether a value is part of a set
# example, math will be removed since it is in there twice

art_courses = {'History', 'Math', 'CompSci', 'Art'}
# Can also be good to compare different sets to see if they share a value

# print(set_courses.intersection(art_courses)) # Shows what course are in both sets
# print(set_courses.difference(art_courses)) # Shows what courses are not in both sets
# print(set_courses.union(art_courses)) # Adds all possible courses contained in both sets without repeating

print(set_courses)

# To create an empty list, you can use [] or list(), same for tuples but with ()
# However, {} will create a dictionary when creating an empty set. Use set() instead

--------------------------

# CS50 Python

# "python intro.py" will run the program from command line

name = input("What's your name? ").strip().title() # Asks for input from the user

# name = name.strip() # Strips whitespace from str
# name = name.title()

print("Hello,", name)
# print(f"Hello, {name}") # This also works
