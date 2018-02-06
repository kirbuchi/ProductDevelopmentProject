# -*- coding: utf-8 -*-
from api import models


def validate_field_options(options, field_type):
    """
    Validate the `field_options` object for a GenericField instance.
    """
    if field_type != models.FieldType.ENUM:
        # we currently only use extra options for the `enum` field type.
        # other field type's options are ignored
        return {}
    if not isinstance(options, dict):
        raise ValueError('field_options must be a dictionary.')
    enum_choices = options.get('choices', [])
    if not isinstance(enum_choices, list) or len(enum_choices) < 1:
        raise ValueError('enum fields must include a list of of "choices".')

    return options

