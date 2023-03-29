import random
import datetime
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from src.config import BOT_NAME
from src.logger import logger
from src.handle_weather import get_weather_info
from src.handle_math import get_math_calc
from src.handle_translate import translate_text_from_input
from src.handle_wolframalpha import get_wolframalpha_response
from src.data_loader import (
    help_general,
    help_math,
    general_responses,
    default_responses,
    excluded_words,
    good_sentiment_responses,
    bad_sentiment_responses
)

def get_help_info(info_type: str) -> str:
    if info_type == 'help':
        return "Here are the things you can ask me:\n" + "\n".join(help_general)
    elif info_type == 'help math':
        return "To use the math command, enter an expression to evaluate:\n" + "\n".join(help_math)
    else:
        return "Invalid info type specified."
    

def get_date_time_info(info_type: str) -> str:
    now = datetime.datetime.now()
    if info_type == 'day':
        return f"Today is {now.strftime('%A, %B %d, %Y')}."
    elif info_type == 'time':
        return f"The current time is {now.strftime('%I:%M %p')}"
    else:
        return "Invalid info type specified."


def tokenize_and_lemmatize(user_input: str) -> str:
    tokens = word_tokenize(user_input)
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    
    return lemmas


def chatbot(user_input: str) -> str:
    logger.info(f'User said: {user_input}')
    
    user_input = user_input.lower()
    lemmas = tokenize_and_lemmatize(user_input)
    response = get_response(user_input, lemmas, general_responses)
    
    logger.info(f'{BOT_NAME} said: {response}')
    
    return response


def get_response(user_input: str, lemmas: str, general_responses: str) -> str:
    if 'help' in user_input:
        response = get_help_info(user_input)
    elif 'help math' in user_input:
        response = get_help_info(user_input)
    elif 'alpha' in user_input:
        response = get_wolframalpha_response(user_input)
    elif "translate" in lemmas:
        response = translate_text_from_input(lemmas)
    elif 'day' in lemmas:
        response = get_date_time_info('day')
    elif 'time' in lemmas:
        response = get_date_time_info('time')
    elif 'weather' in lemmas:
        response = get_weather_info()
    elif 'math' in lemmas and len(lemmas) > 1:
        response = get_math_calc(user_input)
    else:
        response = get_default_response(user_input, lemmas, general_responses)

    return response


def get_default_response(user_input: str, lemmas: str, general_responses: str) -> str:
    if user_input.lower().startswith("i ") or (len(user_input) <= 5 and user_input.lower() not in excluded_words):
        return random.choice(default_responses)

    for key in general_responses.keys():
        if any(lemma in key for lemma in lemmas):
            return random.choice(general_responses[key])

    return get_sentiment_response(user_input)


def get_sentiment_response(user_input: str) -> str:
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    if sentiment > 0.5:
        return random.choice(good_sentiment_responses)
    elif sentiment < -0.5:
        return random.choice(bad_sentiment_responses)
    else:
        return random.choice(default_responses)
