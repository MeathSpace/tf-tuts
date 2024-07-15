def lambda_handler(event, context):
    a = 10
    b = 20
    sum = a + b

    response = {
        "statusCode": 200,
        "body": sum
    }
    return response
