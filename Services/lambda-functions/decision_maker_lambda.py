import json

def lambda_handler(event, context):
    fraud_score = event['fraud_score']
    if fraud_score > 0.8:
        decision = 'Fraud detected'
    else:
        decision = 'No fraud'

    return {
        'statusCode': 200,
        'body': json.dumps({'decision': decision})
    }
