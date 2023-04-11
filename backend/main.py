from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/', methods=['GET'])
def greetings():
  return("Hello, world")

@app.route('/shark', methods=['GET'])
def shark():
  return("This is Shark!")

GAMES = [
  {
  'title': '2k21',
  'genre': 'sports',
  'played': True
  },
  {
  'title': 'Evil Within',
  'genre': 'horror',
  'played': False
  },
  {
  'title': 'The last of us',
  'genre': 'survival',
  'played': True
  },
  {
  'title': 'Days gone',
  'genre': 'horror/survival',
  'played': False
  },
  {
  'title': 'Mario',
  'genre': 'retro',
  'played': True
  },
]

#get route here
@app.route('/games', methods=['GET'])
def all_games():
  return jsonify({
    'games': GAMES,
    'status': 'successs'
  })


if __name__ == "__main__":
  app.run(debug=True)


