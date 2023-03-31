[![CodeFactor](https://www.codefactor.io/repository/github/mafarit/simplechatbot/badge)](https://www.codefactor.io/repository/github/mafarit/simplechatbot)
## Installation

You need to install the following Python packages:
- geocoder
- requests
- textblob
- nltk
- deep_translator
- wolframalpha
- revchatgpt

You can install these packages using the following command:
```
pip install -r requirements.txt
```
## Usage

To use SimpleChatBot, download the executable from the [Releases](https://github.com/MafariT/SimpleChatBot/releases/latest). If you choose to run the executable, you do not need to install Python or any additional packages.

Here are some examples of things you can say to the chatbot:

- help: displays a list of available commands and their descriptions
- gpt [message]: To interact with ChatGPT
- alpha [message]: To interact with WolframAlpha
- translate [text] to [language]: Translates the given text to the specified language
- math [expression]: Calculates the given mathematical expression (help math for more details)
- day: Provides information on the current day
- time: Provides information on the current time
- weather: Provides weather information

        
Additionally, each command has alternative phrasings that can be used to trigger the corresponding action
For example, instead of typing 'time', you can ask 'What time is it?' and the chatbot will provide the current time

To use Weather, WolframAlpha, ChatGPT feature, you need to get the api keys from
- [OpenWeather](https://openweathermap.org/)
- [WolframAlpha](https://products.wolframalpha.com/api/)
- [ChatGPT](https://platform.openai.com/account/api-keys)

You can add it to your ```config.py``` file under ```API_KEY = 'YOUR_API_KEY'```
