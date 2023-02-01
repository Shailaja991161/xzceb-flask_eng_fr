import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

AUTHENTICATOR = IAMAuthenticator(apikey)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version=VERSION, authenticator=AUTHENTICATOR)

LANGUAGE_TRANSLATOR.set_service_url(url)

def englishtofrench(input_text):
    '''This function translates the user_input(english) into french'''

    FRENCH_TRANSLATION = LANGUAGE_TRANSLATOR.translate(
        text= input_text , model_id='en-fr').get_result()

    return FRENCH_TRANSLATION['translations'][0]['translation']

def frenchtoenglish(input_text):
    '''this function translates the user_input(english) into german'''

    ENGLISH_TRANSLATION = LANGUAGE_TRANSLATOR.translate(
        text= input_text , model_id='fr-en').get_result()

    return ENGLiSH_TRANSLATION['translations'][0]['translation']