import json
import threading


def load_data(key: dict) -> dict:
    with open('src/data/chat_data.json', encoding='utf-8') as f:
        data = json.load(f)[key]
    return data

general_responses_thread = threading.Thread(target=lambda: load_data('general_responses'))
default_responses_thread = threading.Thread(target=lambda: load_data('default_responses'))
excluded_words_thread = threading.Thread(target=lambda: load_data('excluded_words'))
good_sentiment_responses_thread = threading.Thread(target=lambda: load_data('good_sentiment_responses'))
bad_sentiment_responses_thread = threading.Thread(target=lambda: load_data('bad_sentiment_responses'))
help_math_thread = threading.Thread(target=lambda: load_data('help_math'))
help_general_thread = threading.Thread(target=lambda: load_data('help_general'))

general_responses_thread.start()
default_responses_thread.start()
excluded_words_thread.start()
good_sentiment_responses_thread.start()
bad_sentiment_responses_thread.start()
help_math_thread.start()
help_general_thread.start()

general_responses_thread.join()
default_responses_thread.join()
excluded_words_thread.join()
good_sentiment_responses_thread.join()
bad_sentiment_responses_thread.join()
help_math_thread.join()
help_general_thread.join()

general_responses = load_data('general_responses')
default_responses = load_data('default_responses')
excluded_words = load_data('excluded_words')
good_sentiment_responses = load_data('good_sentiment_responses')
bad_sentiment_responses = load_data('bad_sentiment_responses')
help_math = load_data('help_math')
help_general = load_data('help_general')
