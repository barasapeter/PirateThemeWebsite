from flask import Flask, render_template

app = Flask(__name__, static_folder="static")


@app.route("/")
def hello():
    name = "Sam"  # Replace this with the name you want to test
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run()
