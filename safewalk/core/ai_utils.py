from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from django.conf import settings

# Setup Azure credentials
vision_client = ComputerVisionClient(
    endpoint=settings.AZURE_VISION_ENDPOINT,
    credentials=CognitiveServicesCredentials(settings.AZURE_VISION_KEY)
)

def analyze_video_frame(image_bytes):
    """
    Analyze the image using Azure Cognitive Services to detect objects and generate captions.
    """
    result = vision_client.analyze_image_in_stream(
        image=image_bytes,
        visual_features=["Objects", "Description"]
    )
    return {
        'objects': [obj.object_property for obj in result.objects],
        'captions': [cap.text for cap in result.description.captions]
    }