#!/bin/env python2.7.6

import csv
import requests
from bs4 import BeautifulSoup
import time
import os

'''
Sets our url to the FBI reading room location, then parses through using bs4 to locate only the links to files we want to download.
'''
url = 'http://m.nationals.mlb.com/roster/'
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
#raw_foias = soup.findAll('dd', attrs='contenttype-folder')

raw_data = soup.findAll('tr')

# For class
# print(soup.prettify())

'''
This loops through each of the foias listed and pulls the links, names and dates into individual lists. * It was getting hung up on the header row. See below. *
'''
names=[] # I changed the name here.
heights=[] 
dobs=[]
for row in raw_data:
    if row.findAll('th'): # Notice here that I skipped the header row. 
            pass # And I'm just having it pass to the next row
    else:   
        name=row.find('a').text # If you take a look at the page, the name is in the link text.
        height=row.find('td', attrs='dg-height').text # Good job here, just had to add 's' to attrs
        dob=row.find('td', attrs='dg-date_of_birth').text # Good job here.
        names.append(str(name))
        heights.append(str(height))
        dobs.append(str(dob))

'''
Next, we zip the lists together into one called docs
'''
docs=zip(names,heights,dobs) # Just different names of our lists.

'''
Creates a new directory called foias if it doesn't exist called nats
'''
directory=os.getcwd()
if not os.path.exists(directory+'/nats'):
    os.makedirs(directory+'/nats')

'''
Assigns the variable "folder" to our path with the newly created directory
'''
folder=directory+'/nats'

'''
Creates a string of the current time in year, month, day and hour format
'''
file_time=time.strftime("%Y%m%d%H")

'''
Creates a new csv of the current list of foias on the FBI's recently added page
'''
with open(folder+"/nats"+file_time+".csv", "w") as outfile: # Python 3 use "w"
    writer = csv.writer(outfile, quotechar='"')
    writer.writerow(['name','height','dob']) # Notice we're creating a header row
    for csv_row in docs: # Remember our loop from before for each row in our docs do X.
        writer.writerow(csv_row)
    print("CSV File Ready") # Print this to the console when we're done.
