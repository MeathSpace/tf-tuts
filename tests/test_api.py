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
    
    assert "message" in response_json, "message key missing in response body"
    assert response_json["message"] == "success", f"Expected message 'success', but got {body['message']}"
    
    assert "sum" in response_json, "sum key missing in response body"
    assert response_json["sum"] == 30, f"Expected sum 30, but got {body['sum']}"

    assert "diff" in response_json, "diff key missing in response body"
    assert response_json["diff"] == 10, f"Expected diff 10, but got {body['diff']}"

    assert "multiply" in response_json, "multiply key missing in response body"
    assert response_json["multiply"] == 200, f"Expected multiply 200, but got {body['multiply']}"

    assert "division" in response_json, "division key missing in response body"
    assert response_json["division"] == 2.0, f"Expected division 2.0, but got {body['division']}"


# import requests
# import allure
 
# @allure.description("Api Test")
# def test_apirequest():
#     resp = requests.request(url="https://google.com", method="GET")
#     print(resp.json)
#     assert int(resp.status_code) == 200