count= dict()
names = ['felo','Apocalipsis','Cabo','felo','cabo','felo']
for name in names:
    count[name]=count.get(name,0) + 1

print(count)

stuff = dict()
print(stuff.get('candy',-1))