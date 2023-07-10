import config
from src import proxy, helpers
from flask import (
    Flask,
    request,
    render_template
)

app = Flask(__name__, static_folder="static", static_url_path="")


@app.route("/")
def index():
    return render_template(
        "index.html",
    )


@app.route("/post", methods=["post"])
def post():
    url = request.form.get("url")
    if url == "":
        return render_template(
            "error.html",
            message="You didn't input a url."
        )

    print(helpers.valid_url(url))

    return render_template(
        "proxy.html",
        content=proxy.proxy_url(
            helpers.valid_url(url)
        )
    )


if __name__ == "__main__":
    app.run(threaded=True, port=config.PORT)
