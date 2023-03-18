import random
import geocoder
import requests
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

# Defining the responses
RESPONSES = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm doing well, thank you.", "I'm fine, thanks for asking.", "I'm good, how about you?"],
    "what's your name": ["My name is Chatbot.", "I'm Chatbot, nice to meet you.", "I go by the name Chatbot."],
    "who are you": ["My name is Chatbot.", "I'm Chatbot, nice to meet you.", "I go by the name Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "how old are you": ["I don't have an age, I'm a chatbot!", "I'm ageless, I'm a chatbot!", "I don't age, I'm a chatbot!"],
    "what's the weather like": [get_weather_info()],
}

# Defining the chatbot function
def chatbot():
    # Greeting message
    print("Hi, I'm a chatbot. What can I help you with today?")
    
    # Chatting loop
    while True:
        # User input
        user_input = input().lower()
        
        # Tokenize the user's input
        tokens = word_tokenize(user_input)
        # Lemmatize the tokens
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(token) for token in tokens]
                
        # Exit condition
        if user_input == "bye":
            response = random.choice(RESPONSES["bye"])
            print(response)
            break
        for key in RESPONSES.keys():
            if any(lemma in key for lemma in lemmas):
                responses = random.choice(RESPONSES[key])
                print(responses)
                break
            # Sentiment analysis
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity
            if sentiment > 0.5:
                response = "That's great to hear!"
                print(response)
                break
            elif sentiment < -0.5:
                response = "I'm sorry to hear that."
                print(response)
                break
        else:
            response = random.choice(["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."])
            print(response)
            
                        
# Calling the chatbot function
chatbot()