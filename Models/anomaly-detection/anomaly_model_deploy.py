import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.model import Model
from sagemaker import serializers, deserializers

sagemaker_session = sagemaker.Session()
role = get_execution_role()

model_path = 's3://your-bucket/anomaly-model/model.tar.gz'

anomaly_model = Model(
    image_uri='your-docker-image-uri',
    model_data=model_path,
    role=role,
    sagemaker_session=sagemaker_session,
    predictor_cls=sagemaker.predictor.RealTimePredictor
)

anomaly_predictor = anomaly_model.deploy(
    initial_instance_count=1,
    instance_type='ml.t2.medium',
    serializer=serializers.JSONSerializer(),
    deserializer=deserializers.JSONDeserializer()
)

print("Anomaly Detection Model Deployed Successfully.")
