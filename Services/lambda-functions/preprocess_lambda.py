import json
from preprocessing.audio_preprocessing import preprocess_audio
from preprocessing.video_preprocessing import preprocess_video
from preprocessing.transaction_cleaning import preprocess_transactions

def lambda_handler(event, context):
    file_key = event['file_key']
    bucket_name = event['bucket_name']
    file_type = event['file_type']

    if file_type == 'audio':
        processed_data = preprocess_audio(file_key, bucket_name)
    elif file_type == 'video':
        processed_data = preprocess_video(file_key, bucket_name)
    elif file_type == 'transaction':
        processed_data = preprocess_transactions(file_key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully')
    }
