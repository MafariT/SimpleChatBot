from deep_translator import GoogleTranslator
from src.logger import logger


def translate_text_from_input(lemmas: str) -> str:
    try:
        # Get the text to translate and the target language
        translate_index = lemmas.index("translate")
        text_to_translate = " ".join(lemmas[translate_index+1:])
        target_language_index = len(lemmas) - lemmas[::-1].index("to") - 1 if "to" in lemmas else -1
        if target_language_index != -1:
            target_language = lemmas[target_language_index+1]
            text_to_translate = " ".join(lemmas[translate_index+1:target_language_index])
        else:
            target_language = "en"
        # Translate the text
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text_to_translate)
    except Exception as e:
        logger.error(f"Error occurred while translating text: {text_to_translate}. Exception: {e}", exc_info=True)
        translated_text = f"An error occurred while translating the text: '{text_to_translate}'. Please check the log file for more information on the error."
    return translated_text