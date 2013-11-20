import json
import os
import imghdr
from PIL import Image
from django.test import SimpleTestCase

from ..utils import draw_signature

DUMMY_VALUE = [{"x": [205, 210], "y": [59, 63]},
               {"x": [205, 207], "y": [67, 64]}]
DUMMY_STR_VALUE = json.dumps(DUMMY_VALUE)


class UtilsTest(SimpleTestCase):

    def test_inputs(self):
        # Bad str value
        self.assertRaises(ValueError, draw_signature, 'foo_bar')
        # Bad type value
        self.assertRaises(ValueError, draw_signature, object())
        # Good list value
        draw_signature(DUMMY_VALUE)
        # Good str value
        draw_signature(DUMMY_STR_VALUE)

    def test_outputs(self):
        # As a file
        output = draw_signature(DUMMY_VALUE, as_file=True)
        self.assertTrue(os.path.isfile(output))
        self.assertIsNotNone(imghdr.what(output))
        # As an Image
        output = draw_signature(DUMMY_VALUE)
        self.assertTrue(issubclass(output.__class__, Image.Image))
        self.assertTrue(all(output.getbbox()))
