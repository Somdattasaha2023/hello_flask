import html
from flask import Flask, render_template

from vsearch import search4letters

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route('/search4')
def do_search()  -> str :
  return str(search4letters('life and hell'))


@app.route('/entry')
def entry_page()  -> 'html' :
    return render_template('entry.html',the_title='welcome to seearch4letters on the web..this is new .....!')



if __name__ == '__main__':
  app.run(debug=True)