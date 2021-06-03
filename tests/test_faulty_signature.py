import json

from django.test import SimpleTestCase

from jsignature.templatetags.jsignature_filters import signature_base64

FAULTY_SIGNATURE = [{"x": [120.00675156801722, 116.11464070635179, 114.16858527551909], "y": [83.0316983821957, 76.54484694608666, 224.44505968937275]}, {"x": [161.52260075911508, 165.4147116207805, 173.84761848772226, 184.2265807854967, 201.0923945193802], "y": [84.97775381302841, 79.78827266414118, 72.00405094081033, 62.922458930257676, 56.43560749414864]}]
DUMMY_STR_VALUE = json.dumps(FAULTY_SIGNATURE)

class TemplateFilterFailedTest(SimpleTestCase):
    def test_throw_error(self):
        output = signature_base64(DUMMY_STR_VALUE)
