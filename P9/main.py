from urllib import request

req = request.Request("http://fanyi.baidu.com/")

response = request.urlopen(req)
html = response.read()    #读取网页信息
html = html.decode('utf-8')  #对网页进行解码
print(html)

