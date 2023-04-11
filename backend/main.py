from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

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

#get route here and post
@app.route('/games', methods=['GET', 'POST'])
def all_games():
  response_object = {'status': 'success'}
  if request.method == "POST":
    #  request.get_json() converts the JSON object into Python data
    post_data = request.get_json()
    GAMES.append({
      'id': uuid.uuid4().hex,
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played')})
    response_object['message'] = 'Game added'
  else:
    response_object['games'] = GAMES
    # jsonify is defined as a functionality within Python’s capability 
    # to convert a json output into a response object 
  return jsonify(response_object)

#The PUT and DELETE route handlers
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
  response_object = {'status': 'success'}
  if request.method == "PUT":
    post_data = request.get_json()
    remove_game(game_id)
    GAMES.append({
      'id': uuid.uuid4().hex,
      'title': post_data.get('title'),
      'genre': post_data.get('genre'),
      'played': post_data.get('played')
    })
    response_object['message'] = 'Game updated'
  if request.method == 'DELETE':
    remove_game(game_id)
    response_object['message'] = "Game removed"
  return jsonify(response_object)


# Removing the game to update / delete
def remove_game(game_id):
  for game in GAMES:
    if game['id'] == game_id:
        GAMES.remove(game)
        return True
  return False


if __name__ == "__main__":
  app.run(debug=True)


