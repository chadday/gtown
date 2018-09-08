import os
import sys
import time


def make_directories(files_root_path):
    '''
    Creates a new directory if it doesn't exist called nats
    Input:
        The file path argument passed to the script
    Output:
        A path to our opinions directory if it didn't exist before.
    '''
    directory=files_root_path
    if not os.path.exists(directory+'/rosters'):
        os.makedirs(directory+'/rosters')
    folder = directory+'/rosters'
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