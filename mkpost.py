#!/usr/bin/env python 

from __future__ import print_function
import sys
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

""" Simple post creator script """

def run():
    ap = ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('-p', 'postname', help='Set post name to create post file')
    
    args = ap.parse_args()






if __name__ == "__main__":
    run()
    print ('**DONE**')
