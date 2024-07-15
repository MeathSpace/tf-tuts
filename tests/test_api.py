import requests
import allure
import json

@allure.description("API Test")
def test_apirequest():
    # Make a request to your Lambda function endpoint
    url = "https://u9tnio6ui4.execute-api.eu-north-1.amazonaws.com/serverless_lambda_stage/hello"
    resp = requests.get(url)
    
    # Check if the request was successful (status code 200)
    assert resp.status_code == 200, f"Expected status code 200, but got {resp.status_code}"
    
    # Parse the JSON response body
    response_json = resp.json()
    print(response_json)
    
    assert "body" in response_json, "body key missing in response"
    body = json.loads(response_json["body"])  # Parse the JSON string in body
    
    assert "message" in body, "message key missing in response body"
    assert body["message"] == "success", f"Expected message 'success', but got {body['message']}"
    
    assert "sum" in body, "sum key missing in response body"
    assert body["sum"] == 30, f"Expected sum 30, but got {body['sum']}"

    assert "diff" in body, "diff key missing in response body"
    assert body["diff"] == 10, f"Expected diff 10, but got {body['diff']}"

    assert "multiply" in body, "multiply key missing in response body"
    assert body["multiply"] == 200, f"Expected multiply 200, but got {body['multiply']}"

    assert "division" in body, "division key missing in response body"
    assert body["division"] == 2.0, f"Expected division 2.0, but got {body['division']}"


# import requests
# import allure
 
# @allure.description("Api Test")
# def test_apirequest():
#     resp = requests.request(url="https://google.com", method="GET")
#     print(resp.json)
#     assert int(resp.status_code) == 200