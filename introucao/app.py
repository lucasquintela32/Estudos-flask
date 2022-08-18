

from email import header

from flask import Flask, Response, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return "<a href='/posts'>POSTS</a>"


@app.route("/redirect")
def redirect2():
    return redirect(url_for("response"))


@app.route("/response")
def response():
    
    return render_template("response.html")


@app.route("/posts")
@app.route("/posts/<int:id>")
def posts(id):
    titulo = request.args.get("Titulo")
    data = dict(
        patch=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        titulo=titulo,
        id=id if id else 0
    )

    return data

if __name__ == "__main__":
    app.run(debug=True)
