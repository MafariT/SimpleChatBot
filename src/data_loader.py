import json
import threading

def load_responses():
    with open('src/data/chat_data.json') as f:
        responses = json.load(f)['responses']
    return responses


def load_default_responses():
    with open('src/data/chat_data.json') as f:
        default_responses = json.load(f)['default_responses']
    return default_responses


def load_excluded_words():
    with open('src/data/chat_data.json') as f:
        excluded_words = json.load(f)['excluded_words']
    return excluded_words


def load_good_sentiment_responses():
    with open('src/data/chat_data.json') as f:
        good_sentiment_responses = json.load(f)['good_sentiment_responses']
    return good_sentiment_responses


def load_bad_sentiment_responses():
    with open('src/data/chat_data.json') as f:
        bad_sentiment_responses = json.load(f)['bad_sentiment_responses']
    return bad_sentiment_responses

responses_thread = threading.Thread(target=load_responses)
default_responses_thread = threading.Thread(target=load_default_responses)
excluded_words_thread = threading.Thread(target=load_excluded_words)
good_sentiment_responses_thread = threading.Thread(target=load_good_sentiment_responses)
bad_sentiment_responses_thread = threading.Thread(target=load_bad_sentiment_responses)

responses_thread.start()
default_responses_thread.start()
excluded_words_thread.start()
good_sentiment_responses_thread.start()
bad_sentiment_responses_thread.start()

responses_thread.join()
default_responses_thread.join()
excluded_words_thread.join()
good_sentiment_responses_thread.join()
bad_sentiment_responses_thread.join()

responses = load_responses()
default_responses = load_default_responses()
excluded_words = load_excluded_words()
good_sentiment_responses = load_good_sentiment_responses()
bad_sentiment_responses = load_bad_sentiment_responses()