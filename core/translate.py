from google.cloud import translate_v2
from flask_babel import _

def translate(text, source_language, target_language):
    try: 
        translate_client = translate_v2.Client()
    except Exception as e:
        print(e)
        return _('Error: the translation service is not configured.')
    result = translate_client.translate(text, target_language=target_language, source_language=source_language, format_="text")
    return result['translatedText']