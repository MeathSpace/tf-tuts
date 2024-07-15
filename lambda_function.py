import json

def lambda_handler(event, context):
    a = 20
    b = 10
    sum_val = a + b
    diff = a - b
    multiply = a * b
    division = a / b  # Note: Division will result in a float in Python 3.x

    # Example data to include in the response
    data = {
        "statusCode": 200,
        "message": "success",
        "sum": sum_val,  # Use a different variable name to avoid conflicts with built-in function names
        "diff": diff,
        "multiply": multiply,
        "division": division
    }

    # Construct the JSON response
    response = { 
        "body": json.dumps(data)  # Convert Python dictionary to JSON string
    }

    return response
