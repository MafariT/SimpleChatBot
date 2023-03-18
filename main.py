import random
from textblob import TextBlob


# Defining the responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm doing well, thank you.", "I'm fine, thanks for asking.", "I'm good, how about you?"],
    "what's your name": ["My name is Chatbot.", "I'm Chatbot, nice to meet you.", "I go by the name Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "what time is it": ["I'm sorry, I don't have a clock.", "I'm not sure, sorry.", "I don't know, sorry."],
    "how old are you": ["I don't have an age, I'm a chatbot!", "I'm ageless, I'm a chatbot!", "I don't age, I'm a chatbot!"],
    "what's the weather like": ["I'm sorry, I don't have access to weather information.", "I'm not sure, sorry.", "I don't know, sorry."],
}

# Defining the chatbot function
def chatbot():
    # Greeting message
    print("Hi, I'm a chatbot. What can I help you with today?")
    
    # Chatting loop
    while True:
        # User input
        user_input = input().lower()
        
        # Exit condition
        if user_input == "bye":
            response = random.choice(responses["bye"])
            print(response)
        
        # Checking for matching responses
        for key in responses.keys():
            if user_input in key:
                response = random.choice(responses[key])
                print(response)
        else:
            # Random response for unknown input
            response = random.choice(["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm not sure what you mean."])
            print(response)
            
        # Sentiment analysis
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment > 0.5:
            response = "That's great to hear!"
            print(response)
        elif sentiment < -0.5:
            response = "I'm sorry to hear that."
            print(response)
                        
# Calling the chatbot function
chatbot()