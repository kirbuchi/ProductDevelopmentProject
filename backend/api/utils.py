# -*- coding: utf-8 -*-
import random
from uuid import uuid4

from api.models import RiskType, GenericField, FieldType


def get_random_field_data():
    """
    Utility function to generate all the parameters to create a GenericField
    instance with random data.
    """
    field_types = [t for t in FieldType]

    field_unique_id = uuid4().hex
    field_type = random.choices(field_types)[0]
    field_options = {}
    if field_type == FieldType.ENUM:
        field_options = { 'choices': ['Choice A', 'Choice B', 'Choice C'] }

    return { 'name': 'Field {}'.format(field_unique_id),
             'description': 'Description for field {}'.format(field_unique_id),
             'type': field_type,
             'options': field_options }


def generate_risk_with_fields(db, risk_type_data):
    """
    Utility function to create the risk and fields as specified via
    `risk_type_data` at the corresponding tables on the `db`.

    The expected `risk_type_data` must have the following form:

    {
        'name': 'Name of risk',
        'description': 'Description of risk',
        'fields': [
            { 'name': 'name of field',
              'type': 'type of field',
              'description': 'field desc',
              'options': { ... } },
            ...
        ]
    }
    """
    risk = RiskType(name=risk_type_data['name'],
                    description=risk_type_data['description'])
    db.session.add(risk)
    for field_data in risk_type_data['fields']:
        field = GenericField(**field_data)
        risk.fields.append(field)
        db.session.add(field)
    db.session.commit()
    return risk


def create_risk(db, risk_name, risk_description, n_fields=0):
    """
    Utility function to create a risk and generate `n_fields` random fields for
    it.

    Returned value is the serialized representation of the risk.
    """
    expected = { 'name': risk_name,
                 'description': risk_description,
                 'fields': [ get_random_field_data()
                             for _ in range(n_fields) ] }

    risk = generate_risk_with_fields(db, expected)
    # now that we have some ids, add them to the `expected` response
    expected['id'] = risk.id
    for field_index, field in enumerate(risk.fields):
        expected['fields'][field_index]['id'] = field.id
        expected['fields'][field_index]['type'] = field.type.value
    return expected
