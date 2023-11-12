import json
import threading

def load_data(key: str) -> dict:
    with open('src/data/chat_data.json', encoding='utf-8') as f:
        data = json.load(f)[key]
    return data

data_keys = ['general_responses', 'default_responses', 'excluded_words', 
            'good_sentiment_responses', 'bad_sentiment_responses', 
            'help_math', 'help_general']

threads = [threading.Thread(target=lambda key=key: load_data(key)) for key in data_keys]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

general_responses, default_responses, excluded_words, good_sentiment_responses, bad_sentiment_responses, help_math, help_general = [load_data(key) for key in data_keys]
