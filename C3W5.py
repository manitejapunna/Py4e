# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:17:41 2020

@author: Mani Teja
"""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
counts_list=list()
url_req = urllib.request.urlopen(url, context=ctx)
data = url_req.read()
tree = ET.fromstring(data)
sum=0
# below commented lines are also working, just an alternative code
#lst = tree.findall('comments/comment')
lst = tree.findall('.//count')
for str in lst:
    #counts_list.append(int(str.find('count').text))
    counts_list.append(int(str.text))
    
for count in counts_list:
    sum+=count

print(sum)
