import random
import geocoder
import requests
import json
import nltk
import datetime
import src.config as config
from deep_translator import GoogleTranslator
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

def get_help_info():
    # Define the usable commands
    with open('src/commands.json', 'r') as f:
        commands = json.load(f)['commands']
    response = "Here are the things you can ask me:\n" + "\n".join(commands)
    return response

def translate_text(text, target_language):
    translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translated_text

def translate_text_from_input(lemmas):
    # Get the text to translate and the target language
    translate_index = lemmas.index("translate")
    text_to_translate = " ".join(lemmas[translate_index+1:])
    target_language_index = lemmas.index("to") if "to" in lemmas else -1
    if target_language_index != -1:
        target_language = lemmas[target_language_index+1]
        text_to_translate = " ".join(lemmas[translate_index+1:target_language_index])
    else:
        target_language = "en"
    # Translate the text
    translated_text = translate_text(text_to_translate, target_language=target_language)
    return translated_text

def get_day_info():
    now = datetime.datetime.now()
    response = f"Today is {now.strftime('%A, %B %d, %Y')}."
    return response

def get_time_info():
    now = datetime.datetime.now()
    response = f"The current time is {now.strftime('%I:%M %p')}"
    return response

def get_weather_info():
    # Get the user's location using geolocation
    g = geocoder.ip('me')
    lat, lon = g.latlng

    # Use the OpenWeatherMap API to get the current weather data for the user's location
    api_key = config.WEATHER_API_KEY
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the weather data and extract the relevant information
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        # Format the weather information into a response
        response = f"The current temperature is {temperature} degrees Celsius with {humidity}% humidity. The weather is {description}."
    else:
        # Handle errors
        response = "Sorry, I couldn't retrieve the weather information at this time."

    return response

def get_math_calc(user_input):
    expression = user_input.split('math ')[1]
    try:
        result = eval(expression)
        response = f"The result of the calculation is {result}!"
    except:
        response = "Sorry, I couldn't perform that calculation."
    return response

def load_responses():
    with open('src/responses.json') as f:
        responses = json.load(f)
    return responses

def tokenize_and_lemmatize(user_input):
    tokens = word_tokenize(user_input)
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

def chatbot():
    # Greeting message
    print(f"{config.BOT_NAME}: Hi, I'm a chatbot. What can I help you with today?")

    responses = load_responses()

    while True:
        # User input
        user_input = input().lower()
        lemmas = tokenize_and_lemmatize(user_input)
        
        # Check if the user wants to translate text
        if "translate" in lemmas:
            translate_text_response = translate_text_from_input(lemmas)
            print(f"{config.BOT_NAME}: {translate_text_response}")
            continue
        
        # Check if the user wants help
        if 'help' in lemmas:
            help_response = get_help_info()
            print(f"{config.BOT_NAME}: {help_response}")
            continue
        
        # Check if the user wants to know the day
        if 'day' in lemmas:
            day_response = get_day_info()
            print(f"{config.BOT_NAME}: {day_response}")
            continue

        # Check if the user wants to know the time
        if 'time' in lemmas:
            time_response = get_time_info()
            print(f"{config.BOT_NAME}: {time_response}")
            continue
        
        # Check if the user asked about the weather
        if 'weather' in lemmas:
            weather_response = get_weather_info()
            print(f"{config.BOT_NAME}: {weather_response}")
            continue
        
        # Check if the user wants to do math
        if 'math' in lemmas and len(lemmas) > 1:
            math_response = get_math_calc(user_input)
            print(f"{config.BOT_NAME}: {math_response}")
            continue

        # Exit condition
        if user_input == "bye":
            response = random.choice(responses["bye"])
            print(f"{config.BOT_NAME}: {response}")
            break

        # Checkfor a matching response
        for key in responses.keys():
            if any(lemma in key for lemma in lemmas):
                response = random.choice(responses[key])
                print(f"{config.BOT_NAME}: {response}")
                break
        else:
            # Sentiment analysis
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity
            if sentiment > 0.5:
                response = "That's great to hear!"
                print(f"{config.BOT_NAME}: {response}")
            elif sentiment < -0.5:
                response = "I'm sorry to hear that."
                print(f"{config.BOT_NAME}: {response}")
            else:
                response = random.choice(["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."])
                print(f"{config.BOT_NAME}: {response}")