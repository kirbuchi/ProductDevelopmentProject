# -*- coding: utf-8 -*-
from api import create_app
from api.models import FieldType
from api.utils import generate_risk_with_fields


demo_risk_types = [
    {
        'name': 'Car Risk',
        'description': 'Risk model used for evaluating car insurance.',
        'fields': [
            { 'name': 'Model',
              'type': FieldType.TEXT,
              'description': 'The model of car.' },
            { 'name': 'Date of manufacture',
              'type': FieldType.DATE,
              'description': 'When was the car manufactured.' },
            { 'name': 'Color',
              'type': FieldType.ENUM,
              'description': 'The color of the car',
              'options': { 'choices': ['Red', 'Green', 'Blue', 'Black'] } },
            { 'name': 'Mileage',
              'type': FieldType.NUMBER,
              'description': 'How many miles are shown in the Odometer.' },
        ]
    },
    {
        'name': 'Real State Property Risk',
        'description': 'Risk model used for evaluating real state insurance.',
        'fields': [
            { 'name': 'Address',
              'type': FieldType.TEXT,
              'description': 'The address of the property.' },
            { 'name': 'Date of construction',
              'type': FieldType.DATE,
              'description': 'When was the building constructed.' },
            { 'name': 'Neighborhood risk profile',
              'type': FieldType.ENUM,
              'description': 'How risky is the neighborhood of the property.',
              'options': {
                  'choices': ['Low risk', 'Medium Risk', 'High Risk',
                              'Very High Risk'],
              }
            },
        ]
    }
]


def create_demo_data():
    _, db = create_app()
    db.create_all()
    for demo_risk in demo_risk_types:
        generate_risk_with_fields(db, demo_risk)


if __name__ == '__main__':
    create_demo_data()
