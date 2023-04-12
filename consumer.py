import json
import binascii
import boto3

def lambda_handler(event, context):
    print(event)
    for record in event['Records']:
        decoded_data=binascii.a2b_base64(record['kinesis']['data'])
        data = json.loads(decoded_data)
        print(type(data))
        print(data)
        print(data['id'],data['name'],data['age'])
 
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('kinesis_datastream_customer_demo')
    
    item = {
        'id': data['id'],
        'name': data['name'],
        'age' : data['age']
    }
    
    table.put_item(Item=item)
