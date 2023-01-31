'''import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'


def englishtofrench(input_text):
    AUTHENTICATOR = IAMAuthenticator(apikey)
    LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version=VERSION, authenticator=AUTHENTICATOR)
    LANGUAGE_TRANSLATOR.set_service_url(url)

    french_translation = LANGUAGE_TRANSLATOR.translate(
        text= input_text , model_id='en-fr').get_result()

    return french_translation['translations'][0]['translation']

def frenchtoenglish(input_text):
    AUTHENTICATOR = IAMAuthenticator(apikey)
    LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version=VERSION, authenticator=AUTHENTICATOR)
    LANGUAGE_TRANSLATOR.set_service_url(url)
    english_translation = LANGUAGE_TRANSLATOR.translate(
        text= input_text , model_id='fr-en').get_result()

    return english_translation['translations'][0]['translation']'''
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

URL_LT="https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/e7f71a8f-5f5a-4f3a-ab51-e395ae28ac0d"
APIKEY_LT = "UKO0UNgWCIWVVRjSV81QXssg7pocf07XNqCgJMcCX4aU"
VERSION = '2018-05-01'

AUTHENTICATOR = IAMAuthenticator(APIKEY_LT)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version=VERSION, authenticator=AUTHENTICATOR)

LANGUAGE_TRANSLATOR.set_service_url(URL_LT)
def englishtofrench(input_text):
    '''This function translates the user_input(english) into french'''

    french_translation = LANGUAGE_TRANSLATOR.translate(
        text= input_text , model_id='en-fr').get_result()

    return french_translation['translations'][0]['translation']

def frenchtoenglish(input_text):
    '''this function translates the user_input(english) into german'''

    english_translation = LANGUAGE_TRANSLATOR.translate(
        text= input_text , model_id='en-de').get_result()

    return english_translation['translations'][0]['translation']
