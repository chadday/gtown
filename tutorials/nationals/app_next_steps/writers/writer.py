import csv

def writer(docs,folder,file_time):
    '''
    Creates a new csv of the current list of foias on the FBI's recently added page
    '''
    with open(folder+"/nats_players"+file_time+".csv", "w") as outfile: # Python 3 use "w"
        writer = csv.writer(outfile, quotechar='"')
        writer.writerow(['jersey','name','bats_throws','height','weight','dob','position']) # Notice we're creating a header row
        for csv_row in docs: # Remember our loop from before for each row in our docs do X.
            writer.writerow(csv_row)
        print("CSV File Ready") # Print this to the console when we're done.
