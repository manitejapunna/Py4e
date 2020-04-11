
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))

html = urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
for i in range(count):
#    print(tags)
    print(tags[position-1].contents[0])
    
    url= tags[position-1].get('href', None)
    html = urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
