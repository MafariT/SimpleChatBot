import wolframalpha
from src.logger import logger
from src.config import WOLFRAMALPHA_API_KEY


def get_wolframalpha_response(user_input: str) -> str:
    try:
        client = wolframalpha.Client(WOLFRAMALPHA_API_KEY)
        query = user_input[6:].strip()
        result = client.query(query)
        if result.success:
            return next(result.results).text
        else:
            return "I'm sorry, I couldn't find an answer to your question"
    except Exception as e:
        logger.error(f"Error occurred while parsing '{query}'. Exception: {e}", exc_info=True)
        return f"An error occurred while parsing '{query}'. Please check the log file for more information on the error"