import requests
import allure
 
@allure.description("Api Test")
def test_apirequest():
    resp = requests.request(url="https://u9tnio6ui4.execute-api.eu-north-1.amazonaws.com/serverless_lambda_stage/hello", method="GET")
    print(resp.json)
    assert int(resp.status_code) == 200