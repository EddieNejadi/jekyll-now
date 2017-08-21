#!/usr/bin/env python 

from __future__ import print_function
import sys, os.path, logging, time
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

""" Simple post creator script """

def run():
    ap = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)
    ap.add_argument('-p', '--postname', required=True, help='Set post name to create post file')
    
    args = ap.parse_args()
    
    pdate = time.strftime("%Y-%m-%d", time.localtime())
    pname = pdate + "-" + args.postname.title() + ".md"
    if os.path.exists("_posts/" + pname):
        logging.error("Post file %s exist", pname)
        exit(1)
    else:
        with open("_posts/" + pname, 'w') as pf:
            pf.write("---\n")
            pf.write("layout: post\n")
            pf.write("title: " + args.postname.replace("_", " ").replace("-", " ").title() + "\n")
            pf.write("date: " + pdate + "\n")
            pf.write("category: Dev\n")
            pf.write("tags: []\n")
            pf.write("summary: \n")
            pf.write("---\n\n\n\n")
            pf.close()
        logging.info("Post %s created", pname)


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    run()
    logging.info("Done")

