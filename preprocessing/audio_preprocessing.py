import boto3
import os
import pydub
from pydub import AudioSegment

s3_client = boto3.client('s3')

def download_audio_from_s3(bucket_name, file_key, local_path):
    s3_client.download_file(bucket_name, file_key, local_path)
    
def convert_audio_format(local_path):
    audio = AudioSegment.from_mp3(local_path)
    wav_path = local_path.replace('.mp3', '.wav')
    audio.export(wav_path, format='wav')
    return wav_path

def preprocess_audio(file_key, bucket_name, local_path='/tmp/'):
    download_audio_from_s3(bucket_name, file_key, local_path)
    converted_file = convert_audio_format(local_path + file_key)
    return converted_file
