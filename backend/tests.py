# -*- coding: utf-8 -*-
import unittest

import api
from api.models import RiskType, GenericField, FieldType


def create_field_types(db):
    field_types = {
        'text': FieldType('text', 'Text type description'),
        'number': FieldType('number', 'Number type description'),
        'date': FieldType('date', 'Date type description'),
        'enum': FieldType('enum', 'Enum type description'),
    }
    db.session.add_all([*field_types.values()])
    db.session.commit()
    return field_types


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
        # create field types
        field_types = create_field_types(self.db)
        # create generic fields
        address_field = GenericField(name='Address',
                                     description='Property\'s address',
                                     field_type=field_types['text'])
        cost_field = GenericField(name='Cost',
                                  description='Current market price for the property',
                                  field_type=field_types['number'])
        build_date_field = GenericField(name='Built Date',
                                        description='The date the house was built',
                                        field_type=field_types['date'])
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
        assert 3 == len(saved_real_state_risk.fields)

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
        field_types = create_field_types(self.db)
        cost_field = GenericField(name='Cost', description='Asset\'s Cost',
                                  field_type=field_types['number'])
        real_state_risk.fields.append(cost_field)
        car_risk.fields.append(cost_field)
        self.db.session.add_all([real_state_risk, car_risk, cost_field])
        self.db.session.commit()

        risk_profiles = RiskType.query.all()
        assert 2 == len(risk_profiles)
        real_state_risk = RiskType.query.filter_by(name=real_state_risk_title).first()
        car_risk = RiskType.query.filter_by(name=car_risk_title).first()
        # each risk type should have a single field
        assert 1 == len(real_state_risk.fields)
        assert 1 == len(car_risk.fields)
        # each risk type's field must be the same
        assert real_state_risk.fields[0] == car_risk.fields[0]

    def test_enum_type_requires_options(self):
        """
        Enum-typed fields may not be created without specifying some options.
        """
        pass


class APITestCase(unittest.TestCase):

    def test_request_risk_type_happy_path(self):
        pass

    def test_request_risk_type_not_found(self):
        pass

    def test_request_risk_type_invalid_id(self):
        pass

    def test_request_risk_type_collection_happy_path(self):
        pass

    def test_request_risk_type_collection_empty(self):
        pass


if __name__ == '__main__':
    unittest.main()
