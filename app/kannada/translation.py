
from googletrans import Translator

translator=Translator()
def get_translation(text:str)->str:
    '''get_translation(text) takes in the kannada text and returns the string of the translated text in english'''
    return translator.translate(text,src='kn',dest='en').text