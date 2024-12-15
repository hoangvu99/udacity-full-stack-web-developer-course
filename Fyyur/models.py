from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#
class Show(db.Model):
    __tablename__ = "show"
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"), primary_key=True)
    start_time = db.Column(db.DateTime, primary_key=True)


class Venue(db.Model):
    __tablename__ = "venue"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    website_link = db.Column(db.String(500))
    seeking_description = db.Column(db.String(500))
    shows = db.relationship("Show", backref="venue")
    seeking_talent = db.Column(db.Boolean, default=False)


class Artist(db.Model):
    __tablename__ = "artist"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean, default=False)
    shows = db.relationship("Show", backref="artist")
    seeking_description = db.Column(db.String(500))
    # DONE: implement any missing fields, as a database migration using Flask-Migrate


# DONE Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
# ----------------------------------------------------------------------------#
# Filters.
# ----------------------------------------------------------------------------#
