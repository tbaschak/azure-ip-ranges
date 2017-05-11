#!/usr/bin/env python

import xmltodict
import sys

if len(sys.argv) != 3:
    print "Usage: %s <xml> <region>" % (sys.argv[0])
else:
    filename = sys.argv[1]
    azureregion = int(sys.argv[2])

    with open(filename) as fd:
        doc = xmltodict.parse(fd.read())
        for iprange in doc['AzurePublicIpAddresses']['Region'][azureregion]['IpRange']:
            print iprange['@Subnet']


