import urllib.request
import urllib.parse
data = {
	's':'basic',
	'submit':'search'
}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
req = urllib.request.Request('http://www.pythonprogramming.net',data)
output = urllib.request.urlopen(req)
print(output.read())
