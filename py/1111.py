t=open('1.txt','r')
a=t.read()
t.close()

print(len(a))
e=''
for i in a.split():
    e=e+i
print(len(e))
