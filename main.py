import random
import geocoder
import requests
import json
import nltk
import datetime
import config
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

def get_help_info():
    # Define the usable commands
    commands = [
        "1. Ask about the weather",
        "2. Ask for the current time",
        "3. Ask for what day is it",
        "4. Do math ('math 1 + 1')",
        "5. Say 'bye' to exit the chatbot",
    ]
    response = "Here are the things you can ask me:\n" + "\n".join(commands)
    return response

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

def load_responses():
    with open('responses.json') as f:
        responses = json.load(f)
    return responses

def chatbot():
    # Greeting message
    print(f"Chatbot: Hi, I'm a chatbot. What can I help you with today?")

    responses = load_responses()

    while True:
        # User input
        user_input = input().lower()

        # Tokenize and lemmatize the user's input
        tokens = word_tokenize(user_input)
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(token) for token in tokens]
        
        # Check if the user wants help
        if 'help' in lemmas:
            help_response = get_help_info()
            print(f"Chatbot: {help_response}")
            continue
        
        # Check if the user wants to know the day
        if 'day' in lemmas:
            day_response = get_day_info()
            print(f"Chabot: {day_response}")
            continue

        # Check if the user wants to know the time
        if 'time' in lemmas:
            time_response = get_time_info()
            print(f"Chatbot: {time_response}")
            continue
        
        # Check if the user asked about the weather
        if 'weather' in lemmas:
            weather_response = get_weather_info()
            print(f"Chatbot: {weather_response}")
            continue
        
        # Check if the user wants to do math
        if 'math' in lemmas and len(lemmas) > 1:
            expression = user_input.split('math ')[1]
            try:
                result = eval(expression)
                response = f"The result of the calculation is {result}!"
            except:
                response = "Sorry, I couldn't perform that calculation."
            print(f"Chatbot: {response}")
            continue

        # Exit condition
        if user_input == "bye":
            response = random.choice(responses["bye"])
            print(f"Chatbot: {response}")
            break

        # Checkfor a matching response
        for key in responses.keys():
            if any(lemma in key for lemma in lemmas):
                response = random.choice(responses[key])
                print(f"Chatbot: {response}")
                break
        else:
            # Sentiment analysis
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity
            if sentiment > 0.5:
                response = "That's great to hear!"
                print(f"Chatbot: {response}")
            elif sentiment < -0.5:
                response = "I'm sorry to hear that."
                print(f"Chatbot: {response}")
            else:
                # If sentiment is neutral, provide a generic response
                response = random.choice(["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."])
                print(f"Chatbot: {response}")
                
if __name__ == '__main__':
    chatbot()