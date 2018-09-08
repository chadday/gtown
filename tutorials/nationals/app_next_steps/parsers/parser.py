import requests
from bs4 import BeautifulSoup

'''
Notice how the libraries are imported in the individual files that use them.
'''

def render_page(url):
    '''
    Sets our url to the Nationals roster, then parses through using bs4 to locate only the links to files we want to download.
    Input:
        Url of the Nationals roster
    Output:
        Soup of our page html
    '''
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    # raw_foias = soup.findAll('dd', attrs='contenttype-folder')
    # raw_foias = soup.findAll('tr')
    return soup

def pos_parser(soup):
    '''
    Let's peel out a chunk of the soup so it's easier to work with our data.
    Now, let's gather the position names into a list. They are located at the top of each table,
    which is not the most convenient. However, we can use some logic later to append these to 
    the appropriate player.
    '''
    raw_positions = soup.findAll('h4') # This grabs the header that contains their positions
    positions=[]
    for i in raw_positions:
        position=str(i.text) # Grabs the position text as a string
        position=position.replace('s','') # Removes the 's' on Pitchers and Catchers
        positions.append(position) # Appends to our list called positions
    return positions

def player_parser(soup,positions):
    '''
    This loops through each of the player tables and pulls out all of their roster information into individual lists. It then zips them together into a list called docs
    '''
    jerseys=[]
    names=[] #
    arms=[]
    heights=[]
    weights=[]
    dobs=[]
    player_pos=[]
    count=0
    raw_tables = soup.findAll('tbody') # This grabs the four tables worth of player info
    for table in raw_tables:
        count=count+1
        rows=table.findAll('tr')
        for row in rows:
            if row.findAll('th'): # Notice here that I skipped the header row.
                pass # And I'm just having it pass to the next row
            else:
                jersey=row.find('td', attrs='dg-jersey_number').text
                name=row.find('a').text #  The name is in the link text.
                arm=row.find('td', attrs='dg-bats_throws').text
                height=row.find('td', attrs='dg-height').text
                weight=row.find('td', attrs='dg-weight').text
                dob=row.find('td', attrs='dg-date_of_birth').text
                '''
                Now we start appending
                '''
                jerseys.append(str(jersey))
                names.append(str(name))
                arms.append(str(arm))
                heights.append(str(height))
                weights.append(str(weight))
                dobs.append(str(dob))
                '''
                This little piece of code below isn't the most elegant but it allows us to use
                the order of the tables to figure out the player positions and append them 
                to our lists.
                '''
                if count==1:
                    player_pos.append(positions[0]) # Pitcher
                if count==2:
                    player_pos.append(positions[1]) # Catcher
                if count==3:
                    player_pos.append(positions[2]) # Infield
                if count==4:
                    player_pos.append(positions[3]) # Outfield
    '''
    Next, we zip the lists together into one called docs
    '''
    docs=zip(jerseys,names,arms,heights,weights,dobs,player_pos) # Just different names of our lists.
    return docs