from flask import Flask, render_template
from post import Post

app = Flask(__name__)

posts = Post()
data = posts.create_post()

@app.route('/')
def home():
    return render_template("index.html", data=data)


@app.route("/blog/<int:num>")
def blog_post(num):
    post_wanted = data[int(num) - 1]
    return render_template("post.html", post=post_wanted)


if __name__ == "__main__":
    app.run(debug=True)
