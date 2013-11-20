import json
from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

from ..fields import JSignatureField
from ..forms import JSignatureField as JSignatureFormField


class JSignatureFieldTest(SimpleTestCase):

    def test_to_python(self):
        f = JSignatureField()
        # Empty values
        for val in ['', [], '[]']:
            self.assertIsNone(f.to_python(val))
        # Correct values
        val = [{"x": [1, 2], "y": [3, 4]}]
        self.assertEquals(val, f.to_python(val))
        val_str = '[{"x":[1,2], "y":[3,4]}]'
        self.assertEquals(val, f.to_python(val_str))
        # Incorrect values
        val = 'foo'
        self.assertRaises(ValidationError, f.to_python, val)

    def test_get_prep_value(self):
        f = JSignatureField()
        # Empty values
        for val in ['', [], '[]']:
            self.assertIsNone(f.get_prep_value(val))
        # Correct values
        val = [{"x": [1, 2], "y": [3, 4]}]
        val_prep = f.get_prep_value(val)
        self.assertIsInstance(val_prep, basestring)
        self.assertEquals(val, json.loads(val_prep))
        val_str = '[{"x":[1,2], "y":[3,4]}]'
        val_prep = f.get_prep_value(val_str)
        self.assertIsInstance(val_prep, basestring)
        self.assertEquals(val, json.loads(val_prep))
        # Incorrect values
        val = type('Foo')
        self.assertRaises(ValidationError, f.get_prep_value, val)

    def test_formfield(self):
        f = JSignatureField()
        cls = f.formfield().__class__
        self.assertTrue(issubclass(cls, JSignatureFormField))
