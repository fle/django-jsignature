import json

from django.test import SimpleTestCase

from jsignature.templatetags.jsignature_filters import signature_base64

DUMMY_VALUE = [{"x": [205, 210], "y": [59, 63]},
               {"x": [205, 207], "y": [67, 64]}]
DUMMY_STR_VALUE = json.dumps(DUMMY_VALUE)


class TemplateFilterTest(SimpleTestCase):
    def test_inputs_bad_type_value(self):
        self.assertEqual(signature_base64(object()), '')
        self.assertEqual(signature_base64(None), '')

    def test_outputs_as_base64(self):
        output = signature_base64(DUMMY_STR_VALUE)
        self.assertEqual(output, "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAABNCAYAAADNYApnAAABIklEQVR4nO3ZP0odURjG4d/ce5dgE3EHgXTp07iD6B7cga3YpUoh7iFrCti4BkGw0OLMoEVIEW4yxPs81ZxzGPial+/8KQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPh3ttW0dhFwCN4GbbNaFXAAlrCdVh/m791KtcC7tmkE7mP1XP2sPs1rQgd7NjVCd1TdNkL3UJ2tWRQciovqqRG8q0aXc6aDPZsat5RVX6q7Rui+zXPbX/wD/KFla7mc306qH9XneazLwZ4s3eu8eqwuV6wF3rXllvK4um9sI7/Oc7s8hMNeLVf/3xthu5nHzmzwF0y9drjrxvPAMgcA/7/lWUBnAwAAAAAAfucFwt4TZmdXW+AAAAAASUVORK5CYII=")
