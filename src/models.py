from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,

        }
    def create(self):
        db.session.add(self)
        db.session.commit()


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=True)
    planet_size = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        return '<Planet %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "planet_size": self.planet_size,


        }
    def create(self):
        db.session.add(self)
        db.session.commit()

class Starship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starship_name = db.Column(db.String(120), unique=True, nullable=True)
    starship_crew = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        return '<Starship %r>' % self.starship_name

    def serialize(self):
        return {
            "id": self.id,
            "starship_name": self.starship_name,
            "starship_crew": self.starship_crew,


        }
    def create(self):
        db.session.add(self)
        db.session.commit()


class FavoritePerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(User)
    persom_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    person = db.relationship(Person)

    def __repr__(self):
        return '<FavoritePerson %r>' % self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,

        }

class FavoritePlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(User)
    planet_name = db.Column(db.String(120), nullable=False)
    planet_size = db.Column(db.String(120), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship(Planet)

    def __repr__(self):
        return '<FavoritePlanet %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "planet_size": self.planet_size,

        }

class FavoriteStarship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(User)
    starship_name = db.Column(db.String(120), nullable=False)
    starship_crew = db.Column(db.String(120), nullable=False)
    starship_id = db.Column(db.Integer, db.ForeignKey("starship.id"))
    starship = db.relationship(Starship)

    def __repr__(self):
        return '<FavoriteStarship %r>' % self.starship_name

    def serialize(self):
        return {
            "id": self.id,
            "starship_name": self.starship_name,
            "starship_crew": self.starship_crew,

        }

