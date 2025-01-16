import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.model import Model
from sagemaker import serializers, deserializers

sagemaker_session = sagemaker.Session()
role = get_execution_role()

model_path = 's3://your-bucket/spam-model/model.tar.gz'

spam_model = Model(
    image_uri='docker-image-uri',
    model_data=model_path,
    role=role,
    sagemaker_session=sagemaker_session,
    predictor_cls=sagemaker.predictor.RealTimePredictor
)

spam_predictor = spam_model.deploy(
    initial_instance_count=1,
    instance_type='ml.t2.medium',
    serializer=serializers.JSONSerializer(),
    deserializer=deserializers.JSONDeserializer()
)

print("Spam Detection Model Deployed Successfully.")
