# -*- coding: utf-8 -*-
import unittest

import api


class ModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app, self.db = api.create_app('test')
        with self.app.test_request_context():
            self.db.create_all()

    def test_risk_types_can_have_multiple_custom_fields(self):
        """
        Multiple fields may be added to a single risk type.
        """
        pass

    def test_fields_can_be_reused_across_risk_types(self):
        """
        A single field may be reused in different risk types.
        """
        pass

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
