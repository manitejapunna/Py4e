# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:37:42 2020

@author: Mani Teja
"""
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numlist=list()
sum=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    numlist.append(tag.contents[0])
#print(numlist)
for a in range(len(numlist)):
    sum=sum+int(numlist[a])
    
print(sum)
    
    
# =============================================================================
# import urllib.request
# 
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())
# =============================================================================
