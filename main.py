import random
import geocoder
import requests
import json
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def get_weather_info():
    # Get the user's location using geolocation
    g = geocoder.ip('me')
    lat, lon = g.latlng

    # Use the OpenWeatherMap API to get the current weather data for the user's location
    api_key = '635e950ebaf0c81a997d2515082f71fd'
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
    print("Hi, I'm a chatbot. What can I help you with today?")

    responses = load_responses()

    while True:
        # User input
        user_input = input().lower()

        # Tokenize and lemmatize the user's input
        tokens = word_tokenize(user_input)
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(token) for token in tokens]
        
        # Check if the user asked about the weather
        if 'weather' in lemmas:
            weather_response = get_weather_info()
            print(weather_response)
            continue

        # Exit condition
        if user_input == "bye":
            response = random.choice(responses["bye"])
            print(response)
            break

        # Checkfor a matching response
        for key in responses.keys():
            if any(lemma in key for lemma in lemmas):
                response = random.choice(responses[key])
                print(response)
                break
        else:
            # If no response has been given yet, provide a generic response
            # Sentiment analysis
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity
            if sentiment > 0.5:
                response = "That's great to hear!"
                print(response)
            elif sentiment < -0.5:
                response = "I'm sorry to hear that."
                print(response)
            else:
                # If sentiment is neutral, provide a generic response
                response = random.choice(["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."])
                print(response)
                
if __name__ == '__main__':
    chatbot()