# import requests
# import allure
# import json

# @allure.description("API Test")
# def test_apirequest():
#     resp = requests.get(url="https://u9tnio6ui4.execute-api.eu-north-1.amazonaws.com/serverless_lambda_stage/hello")
#     response_json = resp.json()
#     print(response_json)
    
#     # Check statusCode
#     assert response_json['statusCode'] == 200
    
#     # Check sum in the body
#     body = response_json['body']
#     assert body['sum'] == 30


import requests
import allure
 
@allure.description("Api Test")
def test_apirequest():
    resp = requests.request(url="https://google.com", method="GET")
    print(resp.json)
    assert int(resp.status_code) == 200