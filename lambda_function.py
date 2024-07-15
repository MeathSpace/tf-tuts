import json

def lambda_handler(event, context):

    a = 20
    b = 10
    sum = a + b
    diff = a - b 
    multiply = a * b
    division = a/b
    # Example data to include in the response
    data = {
        "message": "success",
        "sum": sum,
        "diff" : diff,
        "multiply" : mul,
        "division" : div

    }

    # Construct the JSON response
    response = {
        "statusCode": 200,
        "body": json.dumps(data)  # Convert Python dictionary to JSON string
    }

    return response
