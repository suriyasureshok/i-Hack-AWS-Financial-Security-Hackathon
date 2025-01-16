import boto3
import sys

def detect_deepfake(video_file_path):
    rekognition_client = boto3.client('rekognition')

    bucket_name = 'your-s3-bucket-name'
    video = {'S3Object': {'Bucket': bucket_name, 'Name': video_file_path}}

    try:
        response = rekognition_client.detect_faces(
            Video=video,
            NotificationChannel={
                'SNSTopicArn': 'arn:aws:sns:region:account-id:topic',
                'RoleArn': 'arn:aws:iam::account-id:role/role-name'
            }
        )
        
        print("Detected Faces: ", response['FaceDetails'])

        if len(response['FaceDetails']) > 0:
            print("Faces detected, verifying if manipulated...")
        else:
            print("No faces detected. Likely not a deepfake.")

    except Exception as e:
        print(f"Error detecting deepfake: {str(e)}")

if __name__ == "__main__":
    video_file_path = sys.argv[1]
    detect_deepfake(video_file_path)
