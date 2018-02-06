# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# intermediary table for RiskType to GenericField M2M relationship
risk_types_fields_relationship = db.Table(
    'risk_types_fields',
    db.Column('risk_type_id', db.Integer, db.ForeignKey('risk_types.id'),
              primary_key=True),
    db.Column('generic_field_id', db.Integer,
              db.ForeignKey('generic_fields.id'), primary_key=True)
)


class RiskType(db.Model):
    """
    Holds risk models as configured by insurers.
    """

    __tablename__ = 'risk_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)
    fields = db.relationship('GenericField',
                             secondary=risk_types_fields_relationship)

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<RiskType {}: {}>'.format(self.id, self.name)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "fields": [field.to_dict() for field in self.fields]
        }


class GenericField(db.Model):
    """
    Holds generic fields that can be added to different risk types.
    """

    __tablename__ = 'generic_fields'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)
    field_type_id = db.Column(db.Integer, db.ForeignKey('field_types.id'),
                              nullable=False)
    field_type = db.relationship('FieldType', backref='fields')

    def __init__(self, name, field_type, description=''):
        self.name = name
        self.description = description
        self.field_type = field_type

    def __repr__(self):
        return '<Field {}: {}>'.format(self.id, self.name)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.field_type.code,
        }


class FieldType(db.Model):
    """
    Holds base types for generic fields.
    """

    __tablename__ = 'field_types'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)

    def __init__(self, code, description=''):
        self.code = code
        self.description = description

    def __repr__(self):
        return '<FieldType {}: {}>'.format(self.id, self.code)
