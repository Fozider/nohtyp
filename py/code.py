import json
a=open('q_table.json')
a=json.load(a)
new={}
for i in a:
    m=a[i].index(max(a[i]))
    new[i]=m
print(new)

