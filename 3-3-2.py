import sys
import io
import requests, json

#Rest : post , get , put:update, replace (fetch : update, modify), delete

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

payload1 = {'key1' : 'value1', 'key2' : 'value2'} #dict
payload2 = (('key1','value1'),('key2','value2')) #tuple
payload3 = {'some' : 'nice'}

#r = requests.put('http://httpbin.org/put', data=payload1)
#print(r.text)

#r = requests.put('http://jsonplaceholder.typicode.com/posts/1', data=payload1)
#print(r.text)

r = requests.post('http://www.kma.go.kr/weather/lifenindustry/sevice_rss.jsp', data=payload1)
print(r.text)
