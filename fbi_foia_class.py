#!/bin/env python2.7.6

import csv
import requests
from bs4 import BeautifulSoup
import time
import os

'''
Sets our url to the FBI reading room location, then parses through using bs4 to locate only the links to files we want to download.
'''
url = 'https://vault.fbi.gov/recently-added'
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
raw_foias = soup.findAll('dd', attrs='contenttype-folder')

'''
This loops through each of the foias listed and pulls the links, names and dates into individual lists.
'''
files=[]
links=[]
dates=[]
for row in raw_foias:
	date=row.find('span', attrs='created').text
	file=row.find('h3').text
	link=row.find('a').get('href')
	files.append(str(file))
	links.append(link)
	dates.append(str(date))

'''
Next, we zip the lists together into one called docs
'''  
docs=zip(files,dates,links)

'''
Creates a new directory called foias if it doesn't exist.
'''
directory=os.getcwd()
if not os.path.exists(directory+'/foias'):
	os.makedirs(directory+'/foias')

'''
Assigns the variable "folder" to our path with the newly created directory
'''
folder=directory+'/foias'

'''
Creates a string of the current time in year, month, day and hour format
'''
file_time=time.strftime("%Y%m%d%H")

'''
Creates a new csv of the current list of foias on the FBI's recently added page
'''
with open(folder+"/foias"+file_time+".csv", "wb") as outfile: # Python 3 use "w"
	writer = csv.writer(outfile, quotechar='"')
	writer.writerow(['name','dates','link']) # Notice we're creating a header row
	for csv_row in docs: # Remember our loop from before for each row in our docs do X.
		writer.writerow(csv_row)
	print("CSV File Ready") # Print this to the console when we're done.


