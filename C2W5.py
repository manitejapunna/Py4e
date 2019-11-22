#9.4 Write a program to read through the mbox-short.txt and 
#figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word 
#of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail 
#address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary 
#using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
hand = open(name)
counts=dict()
lst=list()
for line in hand:
    line=line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        if not words[1] in counts:
           counts[words[1]]=1
        else:
           counts[words[1]]=counts[words[1]]+1            
           # counts[words[1]]=counts.get(words[1],1)
bigcount=-1
bigword=None
for a,b in counts.items():
    if bigcount is None or b>bigcount:
        bigword=a
        bigcount=b
print(bigword,bigcount)
