import json
from nodb import NoDB


def hello(event, context):
    nodb = NoDB()
    nodb.bucket = "recuerda"
    nodb.index = "name"
    user = {"name": "Jeff", "age": 19}
    nodb.save(user) # True

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
