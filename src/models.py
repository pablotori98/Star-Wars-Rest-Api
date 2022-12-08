from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False, nullable=False)
    orbital_period = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "Planet name": self.planet_name,
            "climate": self.climate,
            "Rotation Period": self.rotation_period,
            "Orbital period" : self.orbital_period,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.name,
            "Height": self.height,
            "Gender": self.gender,
            "mass" : self.mass,
            # do not serialize the password, its a security breach
        }

class FavouritesPlanet(db.Model):
    __tablename__ = 'favouritesplanets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))


    def __repr__(self):
        return '<Favourites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }

class FavouritesPeople(db.Model):
    __tablename__ = 'tablefavouritesPeople'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def __repr__(self):
        return '<Favourites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "People id": self.people_id,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }