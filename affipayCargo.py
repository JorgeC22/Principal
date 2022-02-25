import http.client
import json

def token():

    conn = http.client.HTTPSConnection("sandbox-tokener.affipay-pagos.net")
    payload = 'grant_type=password&username=alberth1824@hotmail.com&password=484cf4c4623425897319cb900aabb8884976cd284e9939ad7b1a9ced55f38a46'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic Ymx1bW9uX3BheV9lY29tbWVyY2VfYXBpOmJsdW1vbl9wYXlfZWNvbW1lcmNlX2FwaV9wYXNzd29yZA=='
    }
    conn.request("POST", "/oauth/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
    datadecode = data.decode("utf-8")
    jsondata = json.loads(datadecode)
    tokenNew = jsondata["access_token"]
    return tokenNew



#=========================Proceso Cargo==========================================
Token = ""
rutaCheckout = "/checkout/hiDLL8pNJFielKl"


conn = http.client.HTTPSConnection("sandbox-ecommerce.affipay-pagos.net")
payload = "{\n    \"amount\": 15,\n    \"currency\": \"484\",\n    \"customerInformation\": {\n        \"firstName\": \"Hail\",\n        \"lastName\": \"Gonzalez\",\n        \"middleName\": \"\",\n        \"email\": \"user@email.com\",\n        \"phone1\": \"5544332211\",\n        \"city\": \"Mexico\",\n        \"address1\": \"Av. Springfield 6734\",\n        \"postalCode\": \"01620\",\n        \"state\": \"Mexico\",\n        \"country\": \"MX\",\n        \"ip\": \"0.0.0.0\"\n    },\n    \"noPresentCardData\": {\n        \"cardNumber\": \"4242424242424242\",\n        \"cvv\": \"379\",\n        \"cardholderName\": \"Hail A Gonzalez Zepeda\",\n        \"expirationYear\": \"22\",\n        \"expirationMonth\": \"05\"\n    }\n}"
headers = {
  'Authorization': 'Bearer '+Token,
  'Content-Type': 'application/json'
}
conn.request("POST", "/ecommerce/charge", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))