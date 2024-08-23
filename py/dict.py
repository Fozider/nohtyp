import random

file=open('dict.txt','r',encoding='utf-8')
txt=[]
fie=file.read().split('\n')
for i in fie:
    f=i.split(' ')
    txt.append(f[0])
file.close()
print(txt)
num=random.randint(0,len(txt))
print(txt[num])
