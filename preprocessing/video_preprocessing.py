import boto3
import cv2
import os

rekognition_client = boto3.client('rekognition')

def download_video_from_s3(bucket_name, file_key, local_path):
    s3_client = boto3.client('s3')
    s3_client.download_file(bucket_name, file_key, local_path)

def extract_frames_from_video(video_path, frame_rate=1):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_rate == 0:
            frames.append(frame)
        frame_count += 1
    cap.release()
    return frames

def preprocess_video(file_key, bucket_name, local_path='/tmp/'):
    download_video_from_s3(bucket_name, file_key, local_path)
    video_path = local_path + file_key
    frames = extract_frames_from_video(video_path)
    return frames
