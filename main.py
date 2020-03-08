import os

import requests
from flask import Flask, redirect
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText()


@app.route('/')
def home():
    post_url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    fact = get_fact()
    payload = {'input_text': fact }
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    redirect_url = requests.post(post_url, data=payload, headers = user_agent)
    return redirect(redirect_url.url, code = 302)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port, debug='True')

