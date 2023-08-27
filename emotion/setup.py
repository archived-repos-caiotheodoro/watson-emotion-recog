from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features
import os
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv())


def instanciate_watson():
    api_key = os.environ.get('API_KEY')
    service_url = os.environ.get('SERVICE_URL')

    authenticator = IAMAuthenticator(api_key)
    nlu = NaturalLanguageUnderstandingV1(
        version='2023-08-17',  
        authenticator=authenticator
    )
    nlu.set_service_url(service_url)

    emotion_options = EmotionOptions()
    features = Features(emotion=emotion_options)

    return nlu, features