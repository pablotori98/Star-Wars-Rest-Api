"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, People, FavouritesPlanet, FavouritesPeople
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

####################USERS####################

@app.route('/users', methods=['GET'])
def get_users():
    getAllUsers = User.query.all()
    userlist= []
    for singleUser in getAllUsers:
        userlist.append(singleUser.serialize())
    return jsonify(userlist), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    # id = id de User en models ////// user_id = id que obtenemos del endpoint                         
    getUser = User.query.filter_by(id=user_id).first()
    getUser = getUser.serialize()
    return jsonify(getUser), 200


#########################################
#################PLANETS#################
#########################################

@app.route('/planets', methods=['GET'])
def get_planets():
    get_all_planets = Planets.query.all()
    list_planets = []
    for planet in get_all_planets:
        list_planets.append(planet.serialize())
    return jsonify(list_planets)
        
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet_by_id = Planets.query.filter_by(id=planet_id).first()
    planet_by_id = planet_by_id.serialize()
    return jsonify(planet_by_id)

@app.route('/planets', methods=['POST'])
def create_planet():
    data = request.data
    data = json.loads(data)

    newPlanet = Planets(
        planet_name = data['planet_name'],
        orbital_period = data['orbital_period'],
        climate= data['climate'],
        rotation_period= data['rotation_period']
    )
    db.session.add(newPlanet)
    db.session.commit()

    response_planet = {'msg' : 'Nuevo planeta añadido'}

    return jsonify(response_planet)

#Modificar personaje
@app.route('/planets/<int:planet_id>', methods=['PUT'])
def modify_planet(planet_id):
    data = request.data
    data= json.loads(data)
    planetid= Planets.query.filter_by(id=planet_id).first()
    planetid.name = data['planet_name']
    planetid.orbital_period = data['orbital_period']
    planetid.rotation_period = data['rotation_period']
    planetid.climate = data['climate']
    db.session.commit()

    response = {"msg" : "valores modificados con exito"}

    return jsonify(response)

########################################
#################PEOPLE#################
########################################

@app.route('/people', methods=['GET'])
def get_people():
    get_all_people = People.query.all()
    people_list= []
    for person in get_all_people:
        people_list.append(person.serialize())
    return jsonify(people_list)

@app.route('/people/<int:person_id>', methods=['GET'])
def get_person_by_id(person_id):
    person_by_id = People.query.filter_by(id=person_id).first()
    person_by_id = person_by_id.serialize()
    return jsonify(person_by_id)

#Creación de personaje
@app.route('/people', methods=['POST'])
def create_person():
    data = request.data #De esta forma solicitamos todos los datos que recibimos
    data = json.loads(data) #Con json traducimos de formato json a formato python

    #Introducimos en newPerson el objeto que contiene toda la información que tenemos que aportar
    # De acuerdo a flask:
    # Inserting data into the database is a three step process:
    # 1- Create the Python object

    newPerson = People(
        name = data["name"],
        height = data["height"],
        gender = data["gender"],
        mass = data["mass"],

    )
    # 2- Add it to the session
    db.session.add(newPerson)
    # 3- Commit the session
    db.session.commit()
    #agradecemos a los dioses de la programación que funciona con un mensajito
    exito = {
        "msg": "Personaje añadido exitosamente"
    }
    return jsonify(exito), 200

#Modificación de personaje

@app.route('/people/<int:people_id>', methods=['PUT'])
def modify_person(people_id):
    data = request.data
    data= json.loads(data)
    peopleid= People.query.filter_by(id=people_id).first()
    peopleid.name = data['name']
    peopleid.gender = data['gender']
    peopleid.mass = data['mass']
    peopleid.height = data['height']
    db.session.commit()

    response = {"msg" : "valores modificados con exito"}

    return jsonify(response)



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
