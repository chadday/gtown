'''
Introduction to python and basic web scraping
    
    *For this exercise, we'll be using Python 3.6*
    This is probably better as a jupyter notebook but can do that later.
'''

'''
Step 1: Basic maneuvering
'''

'''
Import statements
    
    Some more explanation here.
'''
import csv # Imports a module that lets us read and write csvs
from bs4 import BeautifulSoup # Pulls in the BeautifulSoup4 module from the bs4 package
import requests # Imports requests, a simple and powerful library for https requests in python


'''
Introduction to lists

    Lists are what are known in python as a collection. They are ordered and can be changed. I like to think of them as containers. We will be using a list later on to store the individual records we scrape down from the DC courts website.
    
    In python, text is stored in a datatype called a string. Strings are bytes that represent characters but for our purposes just think of them as ways to store words and letters.

    Numbers are stored in three data types: int, float and complex. We generally use integers (whole numbers) and floats (decimals).
'''

list_of_strings = ['hello', 'world'] # Here we have a list with two string, or text, objects

list_of_nums =  [1, 3, 5, 7, 11] # Here we have a list of five python integers. 

# Python can tell you what type you're working with.

type(list_of_strings) # Tells us this is a list

type(list_of_nums) # Tells us this is a list.

# Or many objects are in your list. 

len(list_of_strings)

len(list_of_nums)

# Or tell you the type of object located in a certain position of your list.

type(list_of_strings[0]) # Tells us the type of the first item in your list of strings which is 'hello'

type(list_of_nums[1]) # Tells us the type of the second item in your list of numbers, which is 3


'''
Printing

    Sometimes we want the python console to display things in the console. For example, the contents of our lists or a specific item in the list. We use print() to do this. Note: In Python2.7, you don't use the (). It's just print. 

'''

print(list_of_strings) # Prints the items in our list of strings.

print(list_of_nums) # Prints the items in our list of numbers.

print(list_of_strings[1]) # Prints the second item in our list of strings

print(list_of_nums[4]) # Prints the fifth item in our list of numbers. Remember that 0 is the first item here in python.


'''
Printing specific ways

    Talk about .join() and .format()

'''


'''
Looping and printing
'''

for i in list_of_strings: # Read: For each item in my list do the following
    print(i) # Print, or display, the item

# Now try the same for our list of numbers. 
    
for n in list_of_nums: 
    print(n)

# Get use to this. We're going to be using it a lot as we build our scraper. Now let's talk about csvs in python.
