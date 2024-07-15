import json

def lambda_handler(event, context):

    a = 10
    b = 20
    sum = a + b
    # Example data to include in the response
    data = {
        "message": "success",
        "sum": sum
    }

    # Construct the JSON response
    response = {
        "statusCode": 200,
        "body": json.dumps(data)  # Convert Python dictionary to JSON string
    }

    return response
