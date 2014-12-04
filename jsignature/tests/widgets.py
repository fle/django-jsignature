import json
from pyquery import PyQuery as pq
import six

from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

from ..widgets import JSignatureWidget
from ..settings import JSIGNATURE_HEIGHT


class JSignatureWidgetTest(SimpleTestCase):

    def test_default_media(self):
        widget = JSignatureWidget()
        media = widget.media
        media_js = list(media.render_js())
        self.assertEqual(2, len(media_js))
        media_js_str = "".join(media_js)
        self.assertIn('jSignature.min.js', media_js_str)
        self.assertIn('django_jsignature.js', media_js_str)
        media_css = list(media.render_css())
        self.assertEquals([], media_css)

    def test_init(self):
        w = JSignatureWidget()
        self.assertEquals({}, w.jsignature_attrs)
        given_attrs = {'width': 300, 'height': 100}
        w = JSignatureWidget(jsignature_attrs=given_attrs)
        self.assertEquals(given_attrs, w.jsignature_attrs)

    def test_build_jsignature_id(self):
        w = JSignatureWidget()
        id = w.build_jsignature_id('foo')
        self.assertEqual('jsign_foo', id)

    def test_build_jsignature_config(self):
        w = JSignatureWidget(jsignature_attrs={'width': 400})
        config = w.build_jsignature_config()
        self.assertEqual(400, config.get('width'))
        self.assertEqual(JSIGNATURE_HEIGHT, config.get('height'))

    def test_prep_value_empty_values(self):
        w = JSignatureWidget()
        for val in ['', [], '[]']:
            self.assertEqual('[]', w.prep_value(val))

    def test_prep_value_correct_values_python(self):
        w = JSignatureWidget()
        val = [{"x": [1, 2], "y": [3, 4]}]
        val_prep = w.prep_value(val)
        self.assertIsInstance(val_prep, six.string_types)
        self.assertEquals(val, json.loads(val_prep))

    def test_prep_value_correct_values_json(self):
        w = JSignatureWidget()
        val = [{"x": [1, 2], "y": [3, 4]}]
        val_str = '[{"x":[1,2], "y":[3,4]}]'
        val_prep = w.prep_value(val_str)
        self.assertIsInstance(val_prep, six.string_types)
        self.assertEquals(val, json.loads(val_prep))

    def test_prep_value_incorrect_values(self):
        w = JSignatureWidget()
        val = type('Foo')
        self.assertRaises(ValidationError, w.prep_value, val)

    def test_render(self):
        w = JSignatureWidget()
        output = w.render(name='foo', value=None)
        # Almost useless :/
        self.assertEqual(1, len(pq('.jsign-wrapper', output)))
        self.assertEqual(1, len(pq('[type=hidden]', output)))

    def test_render_reset_button_true(self):
        w = JSignatureWidget(jsignature_attrs={'ResetButton': True})
        output = w.render(name='foo', value=None)
        self.assertEqual(1, len(pq('[type=button]', output)))

    def test_render_reset_button_false(self):
        w = JSignatureWidget(jsignature_attrs={'ResetButton': False})
        output = w.render(name='foo', value=None)
        self.assertEqual(0, len(pq('[type=button]', output)))
