"""
IBM Watson api testing
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    Translate the english text provided to french
    Returns the french translation
    '''
    #write the code here
    if (english_text == ''): return ''
    json_response = json.dumps(language_translator.translate(text=english_text, source='en', target='fr').get_result())
    french_text = json.loads(json_response)
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    '''
    Translate the french text provided to english
    Returns the english translation
    '''
    #write the code here
    if (french_text == ''): return ''
    json_response = json.dumps(language_translator.translate(text=french_text, source='fr', target='en').get_result())
    english_text = json.loads(json_response)
    return english_text["translations"][0]["translation"]