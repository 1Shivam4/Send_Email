from flask import Flask, render_template
from flask import request
from post import Post
from datetime import datetime
from mail import SendMsg


app = Flask(__name__)

def date_time():
    current_year = datetime.now()
    formatted_time = current_year.strftime('%m-%Y')
    return formatted_time


@app.route('/')
def home():
    posts = Post().all_posts
    return render_template("index.html", posts=posts, year=date_time())

@app.route("/blog/<num>")
def get_blog(num):
    posts = Post().all_posts
    number = int(num) - 1
    return render_template("post.html", post = posts[number], year = date_time())
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        send_mail = SendMsg()

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        send_mail.send_email(name=name, email=email, phone=phone, message=message)

        return render_template('response.html')
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
