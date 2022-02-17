var settings = {
    "url": "https://sandbox-ecommerce.affipay-pagos.net/ecommerce/charge",
    "method": "POST",
    "timeout": 0,
    "headers": {
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "Content-Type": "application/json"
    },
    "data": JSON.stringify({
      "amount": 173.01,
      "currency": "484",
      "customerInformation": {
        "firstName": "Homer",
        "lastName": "Simpson",
        "middleName": "",
        "email": "user@email.com",
        "phone1": "5544332211",
        "city": "Mexico",
        "address1": "Av. Springfield 6734",
        "postalCode": "01620",
        "state": "Mexico",
        "country": "MX",
        "ip": "0.0.0.0"
      },
      "noPresentCardData": {
        "cardNumber": "4915661111113980",
        "cvv": "138",
        "cardholderName": "Homer Simpson",
        "expirationYear": "25",
        "expirationMonth": "03"
      }
    }),
  };
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });