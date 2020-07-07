#counting pattern with dictionaries
fhand=input('Open a file:')
handle=open(fhand)
#.txt File exists, is found.
counts=dict()
for line in handle:
    words=line.split()
    print('Words:', words)
    print('Counting...')
    for word in words:
        counts[word]=counts.get(word, 0)+1
#When the program is run, the above indented block is skipped and we're left with:
#Counts {}
print('Counts', counts)
#pretty sure my issue lies in line 6ish, but I'm at a loss specifically.
