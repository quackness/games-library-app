from flask import Flask, jsonify, request
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
@app.route('/games', methods=['GET', 'POST'])
def all_games():
  response_object = {'status': 'success'}
  if request.method == "POST":
    #  request.get_json() converts the JSON object into Python data
    post_data = request.get_json()
    GAMES.append({
      'id': post_data.get('id'),
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played')})
    response_object['message'] = 'Game added'
  else:
    response_object['games'] = GAMES
    # jsonify is defined as a functionality within Python’s capability 
    # to convert a json output into a response object 
  return jsonify(response_object)

if __name__ == "__main__":
  app.run(debug=True)


