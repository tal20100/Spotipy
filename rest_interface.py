from flask import Flask, request

from search.search import get_all_artists

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def show_artists():
    result = get_all_artists()
    return result


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)
