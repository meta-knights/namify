#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import urllib2
import json
import codecs

f = codecs.open("namics.txt", "w", "utf8")

while True:
    response = urllib2.urlopen("http://www.namics.com/?eID=namics_gdw")
    words = json.loads(response.read())
    for word in words: print unicode(word).encode('utf8')
    for word in words: f.write("%s\n" % word)
    time.sleep(1.1) # new combo is generated every 1s on server
