#Used to make requests
import urllib.request

# x = urllib.request.urlopen('https://www.google.com/')
# print(x.read())


# First way as a post request
# used to parse values into the url
# import urllib.parse


# url = 'https://www.google.com/search'
# values = {'q' : 'python programming tutorials'}
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8') # data should be bytes
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()

# print(respData)


# Second way as a get request
# try:
#     x = urllib.request.urlopen('https://www.google.com/search?q=test')
#     #print(x.read())

#     saveFile = open('noheaders.txt','w')
#     saveFile.write(str(x.read()))
#     saveFile.close()
# except Exception as e:
#     print(str(e))


# Final way to search google
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    # print(headers)
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    print(respData)

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))