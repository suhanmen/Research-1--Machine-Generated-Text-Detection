import http.client as httplib


conn = httplib.HTTPSConnection("api.github.com")

conn.putrequest("GET", "/users/defunkt") # Get 방식, 접근할 사용자 주소
conn.putheader("User-Agent", "MyTest")  # User-Agent 만들기, 내용은 상관없다.
conn.endheaders()

res = conn.getresponse()
headers = res.getheaders()    

                                     
print(res.status, res.reason)

for x in headers:
    print (x)

print(res.read())