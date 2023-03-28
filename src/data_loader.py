import json
import threading

# Define a function to load data from a JSON file
def load_data(key: str) -> dict:
    with open('src/data/chat_data.json', encoding='utf-8') as f:
        data = json.load(f)[key]
    return data

# Define a list of data keys to load
data_keys = ['general_responses', 'default_responses', 'excluded_words', 
            'good_sentiment_responses', 'bad_sentiment_responses', 
            'help_math', 'help_general']

# Create a list of threads to load data in parallel
threads = [threading.Thread(target=lambda key=key: load_data(key)) for key in data_keys]

# Start and join all threads
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Load data from each key into separate variables
general_responses, default_responses, excluded_words, good_sentiment_responses, bad_sentiment_responses, help_math, help_general = [load_data(key) for key in data_keys]
