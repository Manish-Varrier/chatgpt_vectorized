import logging
import openai
from chat_utils import ask
# from my_secrets import OPENAI_API_KEY

if __name__ == "__main__":
    while True:
        user_query = input("Enter your question: ")
        openai.api_key = "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"
        logging.basicConfig(level=logging.WARNING,
                            format="%(asctime)s %(levelname)s %(message)s")
        print(ask(user_query))