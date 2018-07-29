#!/bin/env python2.7.6

'''
Last updated on March 25, 2018 
By Chad Day, AP's Washington Investigative Team
This python script uses BeautifulSoup to scrape down documents posted in the FBI's FOIA reading room.
The script saves only newly posted files and sends email and slack alerts with links to the new files. 
The file names are extracted from the end of each link using rsplit.
'''

import csv
import requests
from bs4 import BeautifulSoup
import time
import os
import sys

reload(sys)
sys.setdefaultencoding('UTF8')

'''
Sets our url to the FBI reading room location, 
then parses through using bs4 to locate only the links to files we want to download.
'''
url = 'https://vault.fbi.gov/recently-added'
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")
raw_foias = soup.findAll('dd', attrs='contenttype-folder')

'''
This loops through each of the foias listed and pulls the links, names and dates into individual lists.
It then zips the lists together into one
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

docs_list=zip(files,dates,links)

'''
Creates a new directory called foias if it doesn't exist.
'''
directory=os.getcwd()
if not os.path.exists(directory+'/foias'):
	os.makedirs(directory+'/foias')

folder=directory+'/foias'

'''
Creates a string of the current time in year, month, day and hour format
'''
file_time=time.strftime("%Y%m%d%H")

'''
Creates a new csv of the current list of foias on the FBI's recently added page
'''
with open(folder+"/foias"+file_time+".csv", "wb") as outfile:
	writer = csv.writer(outfile, quotechar='"')
	writer.writerow(['name','dates','link'])
	for csv_row in docs_list:
		writer.writerow(csv_row)
	print "CSV File Ready"
	
