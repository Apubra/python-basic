try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "Geeksforgeeks"
  
for j in search(query, tld="co.in", num=10, stop=10, pause=2, user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"): 
    print(j) 



# import urllib.request
# import json
# x = urllib.request.urlopen('http://testpy.pickandpaid.com/test/')
# data = x.read()
# JSON_object = json.loads(data.decode('utf-8'))
# # print(JSON_object)

# for data in JSON_object:
#     print(JSON_object[data])