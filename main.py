from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def say_hello():
    random_num = random.randint(0, 9000)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_num, year=year)


@app.route("/guess/<name>")
def guesses_name_age(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    gender = response.json()["gender"]

    response1 = requests.get(url=f"https://api.agify.io?name={name}")
    response1.raise_for_status()
    age = response1.json()["age"]

    appellation = name

    return render_template("guess.html", gender=gender, age=age, name=appellation)


@app.route("/blog")
def blog_post():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json()

    return render_template("blogpost.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
