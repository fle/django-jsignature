import json
import six

from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

from ..fields import JSignatureField
from ..forms import JSignatureField as JSignatureFormField


class JSignatureFieldTest(SimpleTestCase):

    def test_to_python_empty(self):
        f = JSignatureField()
        for val in ['', [], '[]']:
            self.assertIsNone(f.to_python(val))

    def test_to_python_correct_value_python(self):
        f = JSignatureField()
        val = [{"x": [1, 2], "y": [3, 4]}]
        self.assertEquals(val, f.to_python(val))

    def test_to_python_correct_value_json(self):
        f = JSignatureField()
        val = [{"x": [1, 2], "y": [3, 4]}]
        val_str = '[{"x":[1,2], "y":[3,4]}]'
        self.assertEquals(val, f.to_python(val_str))

    def test_to_python_incorrect_value(self):
        f = JSignatureField()
        val = 'foo'
        self.assertRaises(ValidationError, f.to_python, val)

    def test_get_prep_value_empty(self):
        f = JSignatureField()
        for val in ['', [], '[]']:
            self.assertIsNone(f.get_prep_value(val))

    def test_get_prep_value_correct_values_python(self):
        f = JSignatureField()
        val = [{"x": [1, 2], "y": [3, 4]}]
        val_prep = f.get_prep_value(val)
        self.assertIsInstance(val_prep, six.string_types)
        self.assertEquals(val, json.loads(val_prep))

    def test_get_prep_value_correct_values_json(self):
        f = JSignatureField()
        val = [{"x": [1, 2], "y": [3, 4]}]
        val_str = '[{"x":[1,2], "y":[3,4]}]'
        val_prep = f.get_prep_value(val_str)
        self.assertIsInstance(val_prep, six.string_types)
        self.assertEquals(val, json.loads(val_prep))

    def test_get_prep_value_incorrect_values(self):
        f = JSignatureField()
        val = type('Foo')
        self.assertRaises(ValidationError, f.get_prep_value, val)

    def test_formfield(self):
        f = JSignatureField()
        cls = f.formfield().__class__
        self.assertTrue(issubclass(cls, JSignatureFormField))
