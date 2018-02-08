# -*- coding: utf-8 -*-
import enum

import sqlalchemy_jsonfield
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

from api.validators import validate_field_options

db = SQLAlchemy()


class FieldType(enum.Enum):
    TEXT = 'text'
    NUMBER = 'number'
    DATE = 'date'
    ENUM = 'enum'


# intermediary table for RiskType to GenericField M2M relationship
risk_types_fields_relationship = db.Table(
    'risk_types_fields',
    db.Column('risk_type_id', db.Integer, db.ForeignKey('risk_types.id'),
              primary_key=True),
    db.Column('generic_field_id', db.Integer,
              db.ForeignKey('generic_fields.id'), primary_key=True),
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
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'fields': [field.to_dict() for field in self.fields]
        }


class GenericField(db.Model):
    """
    Holds generic fields that can be added to different risk types.
    """

    __tablename__ = 'generic_fields'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)
    type = db.Column(db.Enum(FieldType))
    options = db.Column(sqlalchemy_jsonfield.JSONField())

    def __init__(self, name, type, description='', options=None):
        self.name = name
        self.description = description
        self.type = type
        self.options = options or {}

    def __repr__(self):
        return '<Field {}: {}>'.format(self.id, self.name)

    @validates('options')
    def validate_address(self, key, options):
        return validate_field_options(options, self.type)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type.value,
            'options': self.options,
        }
