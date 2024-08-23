#代码：English turn num
# coding=UTF-8

eng=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
    a=[]
    result1=''
    result2=0
    cod=input('请输入需要加密/解密的密码：')
    try:
        cod=int(cod)
        while cod>=26:
            step=cod%26
            a.append(step)
            cod=cod//26
        a.append(cod)
        
        for i in range(len(a)-1,-1,-1):
            result1+=eng[a[i]]

        print(result1)
        
    except:
        y=0
        for i in cod:
            for e in range(26):
                if i==eng[e]:
                    a.append(e)
        for x in range(len(a)-1,-1,-1):
            s=pow(26,y)
            result2+=a[x]*s
            y+1
        print(result2)
    
