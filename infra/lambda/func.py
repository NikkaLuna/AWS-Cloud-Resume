import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')

def lambda_handler(event, context):
    try:
        # Get the current views count
        response = table.get_item(Key={'id': '0'})
        item = response.get('Item', {})
        views = int(item.get('views', 0))
        views += 1

        # Update the views count in DynamoDB
        table.put_item(Item={'id': '0', 'views': views})

        # Return response with the "Access-Control-Allow-Origin" header
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Set to '*' to allow any origin
            },
            'body': json.dumps({'views': views})
        }

    except Exception as e:
        # Handle general exceptions and return a suitable HTTP error code
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Set to '*' to allow any origin
            },
            'body': json.dumps({'error': str(e)})
        }
