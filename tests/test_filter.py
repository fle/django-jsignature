import json

from django.test import SimpleTestCase

from jsignature.templatetags.jsignature_filters import signature_base64

DUMMY_VALUE = [{"x": [205, 210], "y": [59, 63]}, {"x": [205, 207], "y": [67, 64]}]
DUMMY_STR_VALUE = json.dumps(DUMMY_VALUE)


class TemplateFilterTest(SimpleTestCase):
    def test_inputs_bad_type_value(self):
        self.assertEqual(signature_base64(object()), "")
        self.assertEqual(signature_base64(None), "")

    def test_outputs_as_base64(self):
        output = signature_base64(DUMMY_STR_VALUE)
        self.assertEqual(
            output,
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAcCAYAAACUJBTQAAAAuElEQVR4nO3TMQ4BQRSH8d8uR9AQN5Do9Bo3wB3cQCs6lULcwZkkGmeQSBQU+yZEVIxC7FfNvGTnm7fvP9TU/A0NFN8UPB5eflMwQjvWzZyCMiQ9XLFHP7eoCFEL2xCdMMkleMUMl5AtVN1km1GhShcMcQjRKmqNF9+8JSnd59HFDoPYf9xNuuUUZ8w/PfCZlK4OjqpfNI5aU6bHmWK6DsEm9llmkCjcO1mqopxqv0mK8O92UFPzPjdRMBNmBFDqcwAAAABJRU5ErkJggg==",
        )

    def test_outputs_as_base64_with_singlepoints(self):
        face = [
            {"x": [117], "y": [88]},
            {"x": [140], "y": [83]},
            {
                "x": [116, 121, 125, 129, 134, 139, 142, 145],
                "y": [100, 100, 101, 102, 102, 102, 100, 97],
            },
        ]
        output = signature_base64(json.dumps(face))
        self.assertEqual(
            output,
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADEAAAAnCAYAAACmE6CaAAABmklEQVR4nO3XvUpcQRjG8d9xhYghhYFoIZgmbSCVQlIERAKpAl6GuYrchNeQFLmCRLGytdDCIpUEAmkNxIAfKWYGDrK6c9adXTeZP7zs7izn/ZiZ5505VCqVSuU/oIn2TzCVhbSTfjCxLO5Igzns4BuW49hMroPZMnllk1ahh2dYwUNcKbitSogv+VsSCmmPFaVkkKIrkCglvk46GDbAncRXkhxhT0R8JZiY+Eoy1QXcGx1UxkQjNJKppa23qdy6KekFbMbvI20iTR/rCWfNzAiCpQLm8VU4h97HsbFurWGLSofuPL4IBZzinYyOOOjEbqLDR/gcP69a/51gD/s4xp8+zw+iwblwJ/uIDfyKBezGAi4z/NwaAB4Lyd9mJ/iELbzQ7aL4EgfRzw+sx/Gs953cJe/hectpem4Br/Aaa8IlMfE9WlrNm+I3WI2/t/EBP2PMi8z8RsYi3sQk9vDb4NVLdoi3LV+dWmsX8d0k1kaYseuz/QRPB/hMN+EjnAmzf9nH19i43nK7MnQbLf2amVvMRGe/UqlUyvAXHBNDpT7g8gsAAAAASUVORK5CYII=",
        )
