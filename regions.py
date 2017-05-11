#!/usr/bin/env python

import xmltodict
import sys

if len(sys.argv) != 2:
    print "Usage: %s <xml>" % (sys.argv[0])
else:
    count = 0
    filename = sys.argv[1]

    with open(filename) as fd:
        doc = xmltodict.parse(fd.read())
        for region in doc['AzurePublicIpAddresses']['Region']:
            print ("%d\t%s" % (count, region['@Name']))
            count = count + 1

