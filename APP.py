from flask import Flask, json
import requests
import json
 

movies = [

    {"id": 1, "name": "Harry Potter and the Order of the Phoenix",  "img":"https://bit.ly/2IcnSwz","summary":"Harry Potter and Dumbledore's warning about the return of Lord Voldemort is not heeded by the wizard authorities who, in turn, look to undermine Dumbledore's authority at Hogwarts and discredit Harry"}, 
    {"id": 2, "name": "The Lord of the Rings: The Fellowship of the Ring", "img":"https://bit.ly/2tC1Lcg","summary":"A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed"},
    {"id": 3, "name": "Avengers: Endgame", "img":"https://bit.ly/2Pzczlb","summary":"Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe" }
    
    ]

api = Flask(__name__)

@api.route('/movies', methods=['GET'])
def get_movies():
  return json.dumps(movies)

@api.route('/movies', methods=['POST'])
def post_movies():
  return json.dumps({"success": True}), 201  

if __name__ == '__main__':
    api.run()

    url = "http://127.0.0.1:5000/movies"
 
response = requests.get(url)
data = response.text
parsed = json.loads(data)
print(json.dumps(parsed, indent=4))