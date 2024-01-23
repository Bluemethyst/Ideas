import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_with_model(messages, max_tokens=60):
    response = openai.ChatCompletion.create(
      model="model-gpt-3.5",
      messages=messages,
      max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']

conversation_history = []
while True:
    message = input("User: ")
    conversation_history.append({"role": "system", "content": "User: " + message})
    response = chat_with_model([{"role": "system", "content": "User: " + message}])
    print(f"Bot: {response}")
    conversation_history.append({"role": "assistant", "content": "Bot: " + response})