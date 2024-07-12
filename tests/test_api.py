import requests
import allure
 
@allure.description("Api Test")
def test_apirequest():
    resp = requests.request(url="https://google.com", method="GET")
    print(resp.json)
    assert int(resp.status_code) == 200