#!/usr/bin/env python

import os,sys,time,re,urllib,json


if __name__ == '__main__':

    tally = { 'a':0, 'b':0}

    for x in range(10):

        fp = urllib.urlopen('http://ab.cfapps.io/env' )
        json_str = fp.read()
        result = json.loads(json_str)
        sp = result['systemEnvironment']
        ab = sp['AB']
        tally[ab] = tally[ab] +1
        fp.close()
        print ab

    print str(tally)
