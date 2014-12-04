from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

from ..widgets import JSignatureWidget
from ..forms import JSignatureField


class JSignatureFormFieldTest(SimpleTestCase):

    def test_widget(self):
        f = JSignatureField()
        self.assertIsInstance(f.widget, JSignatureWidget)

    def test_to_python_empty_values(self):
        f = JSignatureField()
        for val in ['', [], '[]']:
            self.assertIsNone(f.to_python(val))

    def test_to_python_correct_values(self):
        f = JSignatureField()
        val = '[{"x":[1,2], "y":[3,4]}]'
        self.assertEquals([{'x': [1, 2], 'y': [3, 4]}], f.to_python(val))

    def test_to_python_incorrect_values(self):
        f = JSignatureField()
        val = 'foo'
        self.assertRaises(ValidationError, f.to_python, val)
