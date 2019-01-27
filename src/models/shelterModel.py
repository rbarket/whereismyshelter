from marshmallow import fields, Schema
import datetime
from . import db

class ShelterModel(db.Model):
    """
    Shelter Model
    """
    # table name
    __tablename__ = 'shelters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    max_capacity = db.Column(db.Integer)
    address = db.Column(db.String(128), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = data.get('password')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return ShelterModel.query.all()

    @staticmethod
    def get_one_user(id):
        return ShelterModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)

class ShelterSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    # TODO: needs to be done after creating model