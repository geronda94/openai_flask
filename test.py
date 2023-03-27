import openai
import json


openai.api_key = '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'


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": "Расскажи по подробнее про библиотеку openai"}])

print(completion.choices[0].message.content)