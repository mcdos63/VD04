from flask import Flask, render_template
import time

app = Flask(__name__)

def get_time():
    return time.strftime("%H:%M", time.localtime())

@app.route("/")
def main():
    with open("./static/1.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return render_template("index.html", current_time=get_time(), content=content)

@app.route("/blog/")
def blog():
    with open("./static/2.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return render_template("blog.html", content=content)

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run()