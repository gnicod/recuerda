import json, boto3, os, decimal
from urllib.parse import unquote
from googletrans import Translator
from pylinguee import Linguee

dynamodb = boto3.resource('dynamodb')
translator = Translator()
linguee = Linguee()

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)

def search(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    query = event['pathParameters']['query']
    src = event['pathParameters']['src']
    dest = event['pathParameters']['dest']
    translated = translator.translate(unquote(query), src=src, dest=dest).text
    try:
        #result = table.scan(ConsistentRead=True)
        body = {
            #"input": event,
            #"results": result.get('Items'),
            "query": query,
            "googleTranslation": translated,
            "linguee": linguee.translate(query)
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
