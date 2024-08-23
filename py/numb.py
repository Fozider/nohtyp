# coding=utf-8
import time
txt=open('质数.txt','w+',encoding='utf-8')
inputer=input('你要计算多少之前的质数（将会在当前文件夹生成质数.txt文件）：')
a=3
long=[2]
flag=True
try:
    for i in range(int(inputer)):
        flag=True
        for e in long:
            if a%e==0:
                flag=False
                break
        if flag:
            long.append(a)
            print(a)
    a+=1


finally:
    txt.write('1')
    for q in long:
        txt.write(',')
        txt.write(str(q))
    txt.close()

 

