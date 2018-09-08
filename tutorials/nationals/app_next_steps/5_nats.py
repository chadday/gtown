#!/bin/env python2.7.6

import os
import sys
from parsers.parser import render_page, pos_parser, player_parser
from writers.writer import writer
from utils.utils import make_directories, make_time


def main(files_root_path):
    '''
    Main function
    '''
    path = files_root_path
    url = 'http://m.nationals.mlb.com/roster/'
    page_soup = render_page(url)
    pos_data = pos_parser(page_soup)
    data = player_parser(page_soup,pos_data)
    new_dir = make_directories(path)
    time_string = make_time()
    writer(data,new_dir,time_string)


if __name__=="__main__":
    try:
        files_root_path = os.path.abspath(sys.argv[1])
        print("Using {} to store downloaded files".format(files_root_path))
        main(files_root_path)
    except IndexError:
        msg = "ERROR: You must invoke this script with a target directory for file artifacts:" +\
            "\n\tpython 4_nats_full_refactor.py /path/to/files"
        print(msg)