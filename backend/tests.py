# -*- coding: utf-8 -*-
import unittest
from uuid import uuid4

from flask import json

import api
from api.models import RiskType, GenericField, FieldType


class ModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app, self.db = api.create_app('test')
        with self.app.test_request_context():
            self.db.create_all()

    def test_risk_types_can_have_multiple_custom_fields(self):
        """
        Multiple fields may be added to a single risk type.
        """
        # create risk type
        real_state_risk = RiskType(
            name='Real State Risk Profile',
            description='Risk model for house/real state insurance'
        )
        # create generic fields
        address_field = GenericField(name='Address',
                                     description='Property\'s address',
                                     type=FieldType.TEXT)
        cost_field = GenericField(name='Cost',
                                  description='Current market price for the property',
                                  type=FieldType.NUMBER)
        build_date_field = GenericField(name='Built Date',
                                        description='The date the house was built',
                                        type=FieldType.DATE)
        # add generic fields to risk type
        real_state_risk.fields.extend([address_field, cost_field, build_date_field])
        # commit
        self.db.session.add_all([real_state_risk,
                                 address_field,
                                 cost_field,
                                 build_date_field])
        self.db.session.commit()
        # query risk type and assert fields are present
        saved_real_state_risk = RiskType.query.first()
        # the risk type should contain all three fields
        self.assertEqual(len(saved_real_state_risk.fields), 3)

    def test_fields_can_be_reused_across_risk_types(self):
        """
        A single field may be reused in different risk types.
        """
        # create two separate risk types
        real_state_risk_title = 'Real State Risk Profile'
        car_risk_title = 'Car Risk Profile'
        real_state_risk = RiskType(name=real_state_risk_title)
        car_risk = RiskType(name=car_risk_title)

        # create a single field and add it to both types
        cost_field = GenericField(name='Cost', description='Asset\'s Cost',
                                  type=FieldType.NUMBER)
        real_state_risk.fields.append(cost_field)
        car_risk.fields.append(cost_field)
        self.db.session.add_all([real_state_risk, car_risk, cost_field])
        self.db.session.commit()

        risk_profiles = RiskType.query.all()
        self.assertEqual(len(risk_profiles), 2)
        real_state_risk = RiskType.query.filter_by(name=real_state_risk_title).first()
        car_risk = RiskType.query.filter_by(name=car_risk_title).first()
        # each risk type should have a single field
        self.assertEqual(len(real_state_risk.fields), 1)
        self.assertEqual(len(car_risk.fields), 1)
        # each risk type's field must be the same
        self.assertEqual(real_state_risk.fields[0], car_risk.fields[0])

    def test_enum_type_happy_path(self):
        """
        Enum-typed fields should receive an extra `options` parameter.
        """
        options = { 'choices': ['One', 'Two', 'Three'] }
        enum_type_field = GenericField('An enum-typed field',
                                       type=FieldType.ENUM,
                                       options=options)
        self.db.session.add(enum_type_field)
        self.db.session.commit()
        saved_field = GenericField.query.first()
        self.assertIsNotNone(saved_field)
        self.assertEqual(saved_field.options, options)

    def test_enum_type_requires_options_dict(self):
        """
        Enum-typed fields may not be created without specifying `options`.
        """
        with self.assertRaises(ValueError):
            enum_type_field = GenericField('Enum field without options',
                                           type=FieldType.ENUM)

    def test_enum_type_requires_options_dict_with_at_least_one_choice(self):
        """
        Enum-typed fields may not be created without specifying some choices in
        the options field.
        """
        with self.assertRaises(ValueError):
            enum_type_field = GenericField('Enum field with empty choices',
                                           type=FieldType.ENUM,
                                           options={ 'choices': [] })

    def test_enum_type_requires_options_dict(self):
        """
        Enum-typed fields require a dictionary as their `options`.
        """
        with self.assertRaises(ValueError):
            enum_type_field = GenericField('Enum field with non-dict options',
                                           type=FieldType.ENUM,
                                           options='not a dictionary')


def add_random_fields(db, risk, n_fields=3):
    expected = []
    field_types = [t for t in FieldType]
    for index in range(n_fields):
        field_unique_id = uuid4().hex
        field_options = {}
        field_type = field_types[index % len(field_types)]
        if field_type == FieldType.ENUM:
            field_options = {
                'choices': ['Choice A', 'Choice B', 'Choice C']
            }

        random_field_data = {
            'name': 'Field {}'.format(field_unique_id),
            'description': 'Description for field {}'.format(field_unique_id),
            'type': field_type,
            'options': field_options,
        }

        field = GenericField(**random_field_data)
        risk.fields.append(field)
        db.session.add(field)
        db.session.commit()

        random_field_data.update({
            'id': field.id, 'type': field.type.value
        })

        expected.append(random_field_data)

    return expected


def create_risk(db, risk_name, risk_description, n_fields=0):
    expected = { 'name': risk_name,
                 'description': risk_description,
                 'fields': [] }
    # create risk
    risk = RiskType(name=risk_name, description=risk_description)
    db.session.add(risk)
    db.session.commit()
    # now that we have an id, add it to the `expected` response
    expected['id'] = risk.id

    # add some fields to the risk
    expected_fields = add_random_fields(db, risk, n_fields)
    # ... make sure the new fields are included in the response
    expected['fields'].extend(expected_fields)

    return expected


class APITestCase(unittest.TestCase):
    """ """

    def setUp(self):
        self.app, self.db = api.create_app('test')
        self.client = self.app.test_client()
        with self.app.test_request_context():
            self.db.create_all()
        self.api_url = '/risk-types/'

    def test_request_risk_type_happy_path(self):
        """
        Requesting an existing risk-type via the API should return a JSON
        object with the expected format.
        """
        expected_response = create_risk(self.db,
                                        risk_name='some risk name',
                                        risk_description='some description',
                                        n_fields=3)
        endpoint_url = '{}{}'.format(self.api_url, expected_response['id'])
        response = self.client.get(endpoint_url)
        # basic sanity checks for response object
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        # verify response format
        parsed_response = json.loads(response.data)
        self.assertEqual(parsed_response, expected_response)

    def test_request_risk_type_not_found(self):
        """
        Requesting a non-existing risk-type via the API should return a 404
        response.
        """
        url = self.api_url + '1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_request_risk_type_collection_happy_path(self):
        """
        Requesting the list of all risk-types should return each with the
        expected format.
        """
        # create multiple risk types
        expected_0 = create_risk(self.db, 'risk0', 'risk0 description', 2)
        expected_1 = create_risk(self.db, 'risk1', 'risk1 description', 3)
        expected_2 = create_risk(self.db, 'risk2', 'risk2 description', 4)
        # expected response should be a list of these risk types
        expected_response = [expected_0, expected_1, expected_2]

        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

        # verify response format
        parsed_response = json.loads(response.data)
        self.assertEqual(parsed_response, expected_response)

    def test_request_risk_type_collection_empty(self):
        """
        Requesting the list of all risk-types should return an empty list if
        there are no risk types.
        """
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        parsed_response = json.loads(response.data)
        self.assertEqual(parsed_response, [])


if __name__ == '__main__':
    unittest.main()
