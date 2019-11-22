#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di=dict()
for line in handle:
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        #print(words[5])
        hour=words[5].split(':')
        #print(hour[0])
        #di[hour[0]]=di.get(di[hour[0]],1)+1
        if hour[0] not in di:
            di[hour[0]]=1
        else:
            di[hour[0]]=di[hour[0]]+1
        #print(hour[0],di[hour[0]])
li=sorted(di.items())
#print(li)
for a in li:
    print(a[0],a[1])
        
