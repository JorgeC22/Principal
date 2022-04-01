<?php
$handle = curl_init('http://192.168.1.68:5000/webhook/webhook002/');

$data = [
    "bin" => "411111",
    "lastFour" =>"1111",
    "cardType" => "DEBITO",
    "brand" => "VISA",
    "bank" => "BANORTE",
    "amount" => "1.23",
    "reference" => "20210120182438251",
    "cardHolder" => "Homer Simpson",
    "authorizationCode" => "483347",
    "operationType" => "VENTA",
    "operationNumber" => 29556,
    "descriptionResponse" => "APROBADA",
    "dateTransaction" => "20/01/2021 18:24:38",
    "authentication" => "unknown",
    "membership" => "8226471",
    "provideResponse" => "SB",
    "codeResponse" => "00"
];

$encodedData = json_encode($data);

curl_setopt($handle, CURLOPT_POST, 1);
curl_setopt($handle, CURLOPT_POSTFIELDS, $encodedData);
curl_setopt($handle, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);

$result = curl_exec($handle);
?>