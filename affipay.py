import http.client

conn = http.client.HTTPSConnection("sandbox-tokener.affipay-pagos.net")
payload = 'grant_type=password&username=user.com&password=password'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': ''
}
conn.request("POST", "/oauth/token", payload, headers)
res = conn.getresponse()
data = res.read()
json = data.decode("utf-8")
print(json)
