#!/usr/bin/python3

import re 
from urllib.parse import urlparse, quote 

pattern = "(\s|/)(.*Python.*)(\s|.pdf)"
inFile = "allbooks.txt"
outFile = "all_python_books.txt"

file1 = open(inFile, "r") ;
file2 = open(outFile, "w");

for line in file1:
	if re.search(pattern, line, re.I ):
		parts = line.rsplit("/", 1)
		formats = "[%s](%s)\n" % (parts[-1].strip(), parts[0] + "/" + quote(parts[1].strip()))
		file2.write(formats)
					


