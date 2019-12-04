import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_315650.txt"
handle = open(name)
li=list()
sum=0
#line=line.rstrip()
for line in handle:
    line=line.rstrip()
    y=re.findall('([0-9]+)',line)
    if len(y)>0:
        for x in y:
            li.append(x)
for each in li:
    sum=sum+int(each)
print(sum)
