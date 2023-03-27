from config import OPENAI_API_KEY
import openai
openai.api_key = OPENAI_API_KEY


def turbo_gpt(req):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": f"{req}"}])

    responce = completion.choices[0].message.content
    return str(responce)


def gpt3(req):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=req,
            max_tokens=4000,
            temperature=0.1,
            n=1,
            stop=None
        )
    return str(response.choices[0].text)