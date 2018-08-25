import itertools
import json, boto3, os, decimal
import uuid

from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def get_user_id(event):
    return event['requestContext']['authorizer']['principalId']


def me(event, context):
    items = table.scan(
        FilterExpression=Attr('user_id').eq(get_user_id(event))
    )['Items']
    langs = []
    try:
        langs = [it['lang'] for it in items if ("lang" in it and it["lang"] is not None)]
    except Exception as e:
        langs = str(e)
    body = {
        "langs": langs
    }
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        "body": json.dumps(body, cls=DecimalEncoder)
    }
    return response


def tags(event, context):
    items = table.scan(
        FilterExpression=Attr('user_id').eq(get_user_id(event))
    )['Items']
    _tags = []
    merged_tags = []
    try:
        _tags = [it['tags'] for it in items if ("tags" in it and it["tags"] is not None)]
        merged_tags = [y for x in _tags for y in x]
    except Exception as e:
        merged_tags = str(e)
    body = {
        "tags": merged_tags
    }
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        "body": json.dumps(body, cls=DecimalEncoder)
    }
    return response


def list(event, context):
    body = {
        "memos": table.scan(
            FilterExpression=Attr('user_id').eq(get_user_id(event))
        )['Items'],
        # "event": event
    }
    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        "body": json.dumps(body, cls=DecimalEncoder)
    }
    return response


def add_memo(event, context):
    try:
        data = json.loads(event["body"])
        body = {
            "user_id": get_user_id(event),
            "uuid": uuid.uuid4().hex,
            "front": data["front"],
            "back": data["back"],
            "tags": data["tags"],
            "lang": data["lang"],
        }
        table.put_item(Item=body)
        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            "body": json.dumps(body, cls=DecimalEncoder)
        }
        return response
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        response = {
            "statusCode": 200,
            "body": message
        }
        return response


def search(event, context):
    query = event['pathParameters']['query']
    src = event['pathParameters']['src']
    dest = event['pathParameters']['dest']
    try:
        # result = table.scan(ConsistentRead=True)
        body = {
            # "results": result.get('Items'),
            "user_id": get_user_id(event),
            "query": query,
        }
        table.put_item(Item=body)
        response = {
            "statusCode": 200,
            "body": json.dumps(body, cls=DecimalEncoder)
        }
        return response
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        response = {
            "statusCode": 200,
            "body": message
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
