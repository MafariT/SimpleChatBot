import json

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