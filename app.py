from flask import Flask, redirect, render_template, request, url_for, session
from api_requests import gpt3, turbo_gpt



app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route("/", methods=("GET", "POST"))
def index():    
    if request.method == "POST":
        req = request.form["animal"]
        session['query'] = req

        
        if request.form["submit"] == "GPT 3":
            response = gpt3(req)
            
        else:
            response = turbo_gpt(req)

        return redirect(url_for("index", result=response, req=f' по запросу :{req}'))

    result = request.args.get("result")
    req = f"на запрос: {session.get('query')}"
    return render_template("index.html", result=result, req=req)


def generate_prompt(animal,req ):
    return str(animal.capitalize())
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
