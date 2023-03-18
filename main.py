# Importing required libraries
import random
import time
import pyttsx3
from textblob import TextBlob

# Initializing text-to-speech engine
engine = pyttsx3.init()

# Defining the responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm doing well, thank you.", "I'm fine, thanks for asking.", "I'm good, how about you?"],
    "what's your name": ["My name is Chatbot.", "I'm Chatbot, nice to meet you.", "I go by the name Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

# Defining the chatbot function
def chatbot():
    # Greeting message
    print("Hi, I'm a chatbot. What can I help you with today?")
    
    # Text-to-speech enabled by default
    tts_enabled = False
    
    # Chatting loop
    while True:
        # User input
        user_input = input().lower()
        
        # Exit condition
        if user_input == "bye":
            response = random.choice(responses["bye"])
            print(response)
            if tts_enabled:
                engine.say(response)
                engine.runAndWait()
            break
        
        # Checking for matching responses
        for key in responses.keys():
            if user_input in key:
                response = random.choice(responses[key])
                print(response)
                if tts_enabled:
                    engine.say(response)
                    engine.runAndWait()
                break
        else:
            # Random response for unknown input
            response = random.choice(["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."])
            print(response)
            if tts_enabled:
                engine.say(response)
                engine.runAndWait()
            
        # Time delay
        time.sleep(1)
        
        # Sentiment analysis
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment > 0.5:
            response = "That's great to hear!"
            print(response)
            if tts_enabled:
                engine.say(response)
                engine.runAndWait()
        elif sentiment < -0.5:
            response = "I'm sorry to hear that."
            print(response)
            if tts_enabled:
                engine.say(response)
                engine.runAndWait()
        
        # Enable/disable text-to-speech
        if user_input == "disable tts":
            tts_enabled = False
            print("Text-to-speech has been disabled.")
        elif user_input == "enable tts":
            tts_enabled = True
            print("Text-to-speech has been enabled.")
            
# Calling the chatbot function
chatbot()