#!/usr/bin/python3

import re 
from urllib.parse import urlparse, quote 

s = input("Enter word to search ")
pattern = '^.*(\\[|\\b|[\\W])%ss?(\\b|[\\W]|\\]).*$' % (s) 
inFile = "allbooks.txt"
outFile = "all_%s_books.txt" %(s) 

file1 = open(inFile, "r") ;
file2 = open(outFile, "w");

count = 0 

for line in file1:
	if re.search(pattern, line, re.I ):
		parts = line.rsplit("/", 1)
		formats = "* [%s](%s)\n" % (parts[-1].strip(), parts[0] + "/" + quote(parts[1].strip()))
		file2.write(formats)
		count += 1					

input("\n\n%d Entries Found : Press Enter To Exit ... " % (count) )
