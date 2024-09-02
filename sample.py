import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('sqs')
    response = client.send_message(
      # add your url
        QueueUrl=".../Insert_details_into_SQS_from_Lambda",
        MessageBody = json.dumps(event["body"]))
    # TODO implement
    return {
        'statusCode': response["ResponseMetadata"]["HTTPStatusCode"],
        'body': json.dumps(response["ResponseMetadata"])
    }
