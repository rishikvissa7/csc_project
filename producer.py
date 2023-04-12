import json
import base64
import boto3

def lambda_handler(event, context):
    
    kinesis = boto3.client('kinesis')
    stream_name = 'kinesis_datastream_demo'
    partition_key = '123'
    filename = 'source.json'
    
    with open(filename, 'r') as f:
        data = json.load(f)
        
        for record in data:
            payload = bytes(json.dumps(record), 'utf-8')
            response = kinesis.put_record(StreamName=stream_name, Data =payload, PartitionKey= partition_key)
            print(response)
