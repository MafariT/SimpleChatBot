import json
import threading


def load_data(key):
    with open('src/data/chat_data.json') as f:
        data = json.load(f)[key]
    return data

responses_thread = threading.Thread(target=lambda: load_data('responses'))
default_responses_thread = threading.Thread(target=lambda: load_data('default_responses'))
excluded_words_thread = threading.Thread(target=lambda: load_data('excluded_words'))
good_sentiment_responses_thread = threading.Thread(target=lambda: load_data('good_sentiment_responses'))
bad_sentiment_responses_thread = threading.Thread(target=lambda: load_data('bad_sentiment_responses'))
commands = threading.Thread(target=lambda: load_data('commands'))

responses_thread.start()
default_responses_thread.start()
excluded_words_thread.start()
good_sentiment_responses_thread.start()
bad_sentiment_responses_thread.start()
commands.start()

responses_thread.join()
default_responses_thread.join()
excluded_words_thread.join()
good_sentiment_responses_thread.join()
bad_sentiment_responses_thread.join()
commands.join()

responses = load_data('responses')
default_responses = load_data('default_responses')
excluded_words = load_data('excluded_words')
good_sentiment_responses = load_data('good_sentiment_responses')
bad_sentiment_responses = load_data('bad_sentiment_responses')
commands = load_data('commands')