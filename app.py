import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future
deployment_name = os.getenv("OPENAI_DEPLOYMENT_NAME")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        response = openai.Completion.create(
            engine=deployment_name,
#            model="text-davinci-003",
            prompt=generate_prompt(topic),
            temperature=0.6,
            max_tokens=100
        )
        print(topic, flush=True)
        print(response, flush=True)
        return redirect(url_for("index", result=response.choices[0].text, topic=topic))
    else:
        topic = request.args.get("topic") 

    result = request.args.get("result")
    return render_template("index.html", result=result, topic=topic)


def generate_prompt(topic):
    return "Give me a single, short, absurd, horrible advice on " + topic
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        topic.capitalize()
    )
