import urllib.request as ur
a=open('word.html','w')
while True:
    url=input('url:')
    try:
        req=ur.Request(url)
        with ur.urlopen(req) as response:
            data=response.read()
            json=data.decode()
            a.write(json)
    except:
        print('error')
        continue
    break
a.close()
