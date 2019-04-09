from urllib.request import urlopen
content = urlopen('http://127.0.0.1:5000/api?param1=b&param2=2').read()
print(content)
