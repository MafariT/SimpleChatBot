from revChatGPT.V3 import Chatbot
from src.logger import logger
from src.config import CHATGPT_API_KEY


# Initialize ChatGPT
chatgpt = Chatbot(api_key=CHATGPT_API_KEY,
                engine="gpt-3.5-turbo",
                proxy=None,
                timeout=1.0,
                max_tokens=4096,
                temperature=0.5,
                top_p=1.0,
                presence_penalty=0.0,
                frequency_penalty=0.0,
                reply_count=1,
                system_prompt="You are ChatGPT, a large language model trained by OpenAI. Respond conversationally")


def gpt(user_input :str) -> str:
    try:
        message = user_input[4:].strip()
        chatgpt.ask(prompt=message, role="user", convo_id="default")
        responses = chatgpt.conversation["default"][-1]["content"]
    except Exception as e:
        logger.error(f"Error occurred while parsing '{message}'. Exception: {e}", exc_info=True)
        responses = f"An error occurred while parsing '{message}'. Please check the log file for more information on the error"
    
    return responses