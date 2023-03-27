import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        req = request.form["animal"]
        # response = openai.Completion.create(
        #     model="gpt-3.5-turbo-0301"
        #     prompt=req,
        #     max_tokens=4000,
        #     temperature=0.1,
        #     n=1,
        #     stop=None
        # )
        #return redirect(url_for("index", result=response.choices[0].text))
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": f"{req}"}])

        ret_responce = completion.choices[0].message.content


        return redirect(url_for("index", result=ret_responce))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return str(animal.capitalize())
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
