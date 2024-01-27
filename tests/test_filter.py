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
        self.assertEqual(output, "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAcCAYAAACUJBTQAAAAuElEQVR4nO3TMQ4BQRSH8d8uR9AQN5Do9Bo3wB3cQCs6lULcwZkkGmeQSBQU+yZEVIxC7FfNvGTnm7fvP9TU/A0NFN8UPB5eflMwQjvWzZyCMiQ9XLFHP7eoCFEL2xCdMMkleMUMl5AtVN1km1GhShcMcQjRKmqNF9+8JSnd59HFDoPYf9xNuuUUZ8w/PfCZlK4OjqpfNI5aU6bHmWK6DsEm9llmkCjcO1mqopxqv0mK8O92UFPzPjdRMBNmBFDqcwAAAABJRU5ErkJggg==")
