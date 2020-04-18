"""
    Provides a django model field to store a signature captured
    with jSignature jQuery plugin
"""
import json

from django.db import models
from django.core.exceptions import ValidationError

from .forms import (
    JSignatureField as JSignatureFormField,
    JSIGNATURE_EMPTY_VALUES,
)

try:
    from django.utils import six

    string_types = six.string_types
except ImportError:
    string_types = str


class JSignatureField(models.Field):
    """
    A model field handling a signature captured with jSignature
    """
    description = "A signature captured with jSignature"

    def get_internal_type(self):
        return 'TextField'

    def to_python(self, value):
        """
        Validates that the input can be red as a JSON object. Returns a Python
        datetime.date object.
        """
        if value in JSIGNATURE_EMPTY_VALUES:
            return None
        elif isinstance(value, list):
            return value
        try:
            return json.loads(value)
        except ValueError:
            raise ValidationError('Invalid JSON format.')

    def get_prep_value(self, value):
        if value in JSIGNATURE_EMPTY_VALUES:
            return None
        elif isinstance(value, string_types):
            return value
        elif isinstance(value, list):
            return json.dumps(value)
        raise ValidationError('Invalid format.')

    def formfield(self, **kwargs):
        defaults = {'form_class': JSignatureFormField}
        defaults.update(kwargs)
        return super(JSignatureField, self).formfield(**defaults)
