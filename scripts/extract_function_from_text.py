#! /usr/bin/env python3
import os
import re

final_file = {}

for file in os.listdir("./"):
    if file.endswith(".pcap"):
        f = open("%s" % file, 'r')
        content = f.read()
        f.close()
        number = int(re.search(r'//file([0-9]*)', content).group(1))
        final_file[number] = content

with open("main.c", 'wa+') as file:
    for i, content in sorted(final_file.items()):
        file.write(content)
        file.write("\n")        
    file.close()