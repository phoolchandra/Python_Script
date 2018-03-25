import sys
import os
import re
from HTMLParser import HTMLParser


f = open("testCollection.dat", 'r')

inRecordingMode = False


class MyHTMLParser(HTMLParser):


    def handle_data(self, data):
        self.output.append(data)

    def feed(self, data):
        self.output = []
        HTMLParser.feed(self, data)    


for line in f:

    name = re.search("<title>(.*?)</title>",line)
    if name:
        parser = MyHTMLParser()
        parser.feed(name.group())
        a = ''.join(parser.output) + ".txt"
        print a
        f1 = open(a,'w')

    if not inRecordingMode:
        if line.startswith('<text>'):
            inRecordingMode = True
    elif line.startswith('</text>'):
        inRecodingMode = False
        f1.close()
    else:
        f1.write(line) 


f.close()                   
