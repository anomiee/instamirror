#!/usr/bin/env python
# encoding: utf-8

import sys
import savepagenow
import archiveis

def mirror(url):
    archiveis_url = archiveis.capture(url)
    archiveorg_url = savepagenow.capture_or_cache(url)
    print("URL archived at {0} and {1}".format(archiveis_url, archiveorg_url[0]))

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        mirror(sys.argv[1])    
    else:
        print("Please enter a URL")
        
    
