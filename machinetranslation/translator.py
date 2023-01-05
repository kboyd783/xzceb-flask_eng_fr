"""docstring"""

##import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('8hd5Nw2PVGkJyUYHfiG3s-oU8zHSyuxNIhhVamCttHgQ')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/14182991-29a2-423f-97fe-cd320490d3db')


def english_to_french(english_text):
    """docstring"""

    #write the code here
    frenchtranslation = language_translator.translate(
    text=english_text, model_id='en-fr').get_result()
    return frenchtranslation
    

def french_to_english(french_text):
    """docstring"""
    #write the code here
    englishtranslation = language_translator.translate(
    text=french_text, model_id='fr-en').get_result()
    return englishtranslation