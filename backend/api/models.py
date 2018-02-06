# -*- coding: utf-8 -*-
import enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

import sqlalchemy_jsonfield

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
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "fields": [field.to_dict() for field in self.fields]
        }

def validate_field_options(options, field_type):
    """
    Validate the `field_options` object.
    """
    if field_type != FieldType.ENUM:
        # we currently only use extra options for the `enum` field type.
        # other field type's options are ignored
        return {}
    if not isinstance(options, dict):
        raise ValueError('field_options must be a dictionary.')
    enum_choices = options.get('choices', [])
    if not isinstance(enum_choices, list) or len(enum_choices) < 1:
        raise ValueError('enum fields must include a list of of "choices".')

    return options


class GenericField(db.Model):
    """
    Holds generic fields that can be added to different risk types.
    """

    __tablename__ = 'generic_fields'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    description = db.Column(db.Text)
    field_type = db.Column(db.Enum(FieldType))
    field_options = db.Column(sqlalchemy_jsonfield.JSONField())

    def __init__(self, name, field_type, description='', field_options=None):
        self.name = name
        self.description = description
        self.field_type = field_type
        self.field_options = field_options or {}

    def __repr__(self):
        return '<Field {}: {}>'.format(self.id, self.name)

    @validates('field_options')
    def validate_address(self, key, field_options):
        return validate_field_options(field_options, self.field_type)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.field_type.code,
        }
