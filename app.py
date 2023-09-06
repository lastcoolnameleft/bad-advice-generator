import os, openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_ENDPOINT")
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future
deployment_name = os.getenv("OPENAI_DEPLOYMENT_NAME")

@app.route("/", methods=("GET", "POST"))
def index():
    title = "Bad Advice As A Service (BaaaS)"
    post_path = "/"
    if request.method == "POST":
        topic = request.form["topic"]
        advice = create_oai_completion(deployment_name, topic)
        return redirect(url_for("index", result=advice, topic=topic))
    else:
        topic = request.args.get("topic") 

    result = request.args.get("result")
    return render_template("index.html", result=result, topic=topic, title=title, post_path=post_path)


def create_oai_completion(engine, topic):
    print(topic, flush=True)
    response = openai.Completion.create(
        engine=deployment_name,
        prompt=generate_prompt(topic),
        temperature=0.6,
        max_tokens=100
    )
    print(response, flush=True)
    result = response.choices[0].text.strip()
    return result


def generate_prompt(topic):
    return "Give me a single, short, absurd, horrible advice on " + topic