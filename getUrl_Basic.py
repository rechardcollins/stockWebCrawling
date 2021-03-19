import urllib.request
from urllib import parse

f = urllib.request.urlopen('http://www.python.org/')

print(f.read(300)) # 300byte만 읽어온다.


req = urllib.request.urlopen("https://madplay.github.io")
req.read().decode("utf-8")


print('#'*10 + " Get Header Info")
req = urllib.request.urlopen("https://madplay.github.io")
headerInfo = req.getheader('content-type')
print(headerInfo)

print('#'*10 + " Get HTTP Status")
req = urllib.request.urlopen("https://madplay.github.io")
print(req.status)

print('#'*10 + " Handle URL, Parameter by \'urllib.parse\'")
print('-'*10 + " URL Parsing ")
url = parse.urlparse("https://madplay.github.io/post/java-kafka-example?test=hi")
print(url)
print('-'*10 + " Query String ")
url = parse.urlparse("https://madplay.github.io/post/java-kafka-example?test=hi")
print (parse.parse_qs(url.query))
parse.parse_qs(url.query)['test'][0]        # dictionary Type
print('-'*10 + " Encoding ")
url = parse.urlparse("https://madplay.github.io/post/java-kafka-example?test=hi")
enCoding = parse.quote_plus("김탱은 블로그 주인")
print(enCoding)
enCoding = parse.quote("김탱은 블로그 주인")
print(enCoding)
