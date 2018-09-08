#!/bin/env python2.7.6

import csv
import requests
from bs4 import BeautifulSoup
import time
import os
import sys

def main(files_root_path):
    '''
    Main function
    '''
    path = files_root_path
    url = 'http://m.nationals.mlb.com/roster/'
    page = render_page(url)
    data = parser(page)
    new_dir = make_directories(path)
    time_string = make_time()
    writer(data,new_dir,time_string)

def render_page(url):
    '''
    Sets our url to the FBI reading room location, then parses through using bs4 to locate only the links to files we want to download.
    Input:
        Url of the Nationals roster
    Output:
        Bs4 object of table rows
    '''
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    # For class
    # print(soup.prettify())
    raw_data = soup.findAll('tr')
    return raw_data

def parser(raw_data):
    '''
    This loops through each of the foias listed and pulls the links, names and dates into individual lists. * It was getting hung up on the header row. See below. *
    Input:
        Our bs4 object of raw tables rows
    Output:
        A zipped list of our names, heights and dobs of the players.
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
    return docs

def make_directories(files_root_path):
    '''
    Creates a new directory called foias if it doesn't exist called nats
    Input:
        The file path argument passed to the script
    Output:
        A path to our opinions directory if it didn't exist before.
    '''
    directory=files_root_path
    if not os.path.exists(directory+'/nats'):
        os.makedirs(directory+'/nats')
    folder = directory+'/nats'
    '''
    Assigns the variable "folder" to our path with the newly created directory
    '''
    return folder

def make_time():
    '''
    Creates a string of the current time in year, month, day and hour format
    '''
    file_time=time.strftime("%Y%m%d%H")
    return file_time

def writer(docs,folder,file_time):
    '''
    Creates a new csv of the current list of Nationals players info
    '''
    with open(folder+'/nats'+file_time+".csv", "w") as outfile: # Python 3 use "w"
        writer = csv.writer(outfile, quotechar='"')
        writer.writerow(['name','height','dob']) # Notice we're creating a header row
        for csv_row in docs: # Remember our loop from before for each row in our docs do X.
            writer.writerow(csv_row)
        print("CSV File Ready") # Print this to the console when we're done.

if __name__=="__main__":
    try:
        files_root_path = os.path.abspath(sys.argv[1])
        print("Using {} to store downloaded files".format(files_root_path))
        main(files_root_path)
    except IndexError:
        msg = "ERROR: You must invoke this script with a target directory for file artifacts:" +\
            "\n\tpython fbi_foia.py /path/to/files"
        print(msg)