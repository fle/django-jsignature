import json

from django import forms
from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

from jsignature.fields import JSignatureField
from jsignature.forms import JSignatureField as JSignatureFormField
from tests.models import JSignatureTestModel


class JSignatureFieldTest(SimpleTestCase):

    def test_to_python_empty(self):
        f = JSignatureField()
        for val in ['', [], '[]']:
            self.assertIsNone(f.to_python(val))

    def test_to_python_correct_value_python(self):
        f = JSignatureField()
        val = [{"x": [1, 2], "y": [3, 4]}]
        self.assertEqual(val, f.to_python(val))

    def test_to_python_correct_value_json(self):
        f = JSignatureField()
        val = [{"x": [1, 2], "y": [3, 4]}]
        val_str = '[{"x":[1,2], "y":[3,4]}]'
        self.assertEqual(val, f.to_python(val_str))

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
        self.assertIsInstance(val_prep, str)
        self.assertEqual(val, json.loads(val_prep))

    def test_get_prep_value_correct_values_json(self):
        f = JSignatureField()
        val = [{"x": [1, 2], "y": [3, 4]}]
        val_str = '[{"x":[1,2], "y":[3,4]}]'
        val_prep = f.get_prep_value(val_str)
        self.assertIsInstance(val_prep, str)
        self.assertEqual(val, json.loads(val_prep))

    def test_get_prep_value_incorrect_values(self):
        f = JSignatureField()
        val = type('Foo')
        self.assertRaises(ValidationError, f.get_prep_value, val)

    def test_formfield(self):
        f = JSignatureField()
        cls = f.formfield().__class__
        self.assertTrue(issubclass(cls, JSignatureFormField))

    def test_modelform_media(self):
        class TestModelForm(forms.ModelForm):
            class Meta:
                model = JSignatureTestModel
                fields = forms.ALL_FIELDS

        form = TestModelForm()
        self.assertIn('jSignature.min.js', str(form.media))
        self.assertIn('django_jsignature.js', str(form.media))
