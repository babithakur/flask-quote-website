from flask import Flask, render_template, url_for
import requests
import json
import random
app = Flask(__name__)

@app.route('/')
def indexPage():
    quote_id = random.randint(1, 20)
    get_quote = requests.get("http://127.0.0.1:8000/" + str(quote_id))
    quote = get_quote.json()['quote']
    return render_template('index.html', a=quote)


if __name__ == '__main__':
    app.run(debug=True)
