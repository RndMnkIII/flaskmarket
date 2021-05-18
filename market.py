# market.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

#Dynamic route
@app.route('/about/<username>')
def about(username):
    return f'<h1>This is the about page of {username}</h1>'

if __name__ == "__main__":
    app.run(host='rndmnkiii.com', port='4000', debug=True)

