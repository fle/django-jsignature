"""
    Provides a django form widget to handle a signature capture field with
    with jSignature jQuery plugin
"""
import json
from django.forms.widgets import HiddenInput
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from jsignature.settings import JSIGNATURE_DEFAULT_CONFIG

JSIGNATURE_EMPTY_VALUES = validators.EMPTY_VALUES + ('[]', )


class JSignatureWidget(HiddenInput):
    """
    A widget handling a signature capture field with with jSignature
    """

    # Actually, this widget has a display so we want it to behave like a
    # normal field, not a hidden one
    is_hidden = False

    class Media:
        js = ('js/jSignature.min.js',
              'js/django_jsignature.js')

    def __init__(self, attrs=None, jsignature_attrs=None):
        super(JSignatureWidget, self).__init__(attrs)
        # Store jSignature js config
        self.jsignature_attrs = jsignature_attrs or {}

    def build_jsignature_config(self):
        """ Build javascript config for jSignature initialization.
            It's a dict with for which default values come from settings
            and can be overriden by jsignature_attrs, given at widget
            instanciation time """
        jsignature_config = JSIGNATURE_DEFAULT_CONFIG.copy()
        jsignature_config.update(self.jsignature_attrs)
        return jsignature_config

    def build_jsignature_id(self, name):
        """ Build HTML id for jsignature container.
            It's important because it's used in javascript code """
        return 'jsign_%s' % name

    def prep_value(self, value):
        """ Prepare value before effectively render widget """
        if value in JSIGNATURE_EMPTY_VALUES:
            return "[]"
        elif isinstance(value, basestring):
            return value
        elif isinstance(value, list):
            return json.dumps(value)
        raise ValidationError('Invalid format.')

    def render(self, name, value, attrs=None):
        """ Render widget """
        # Build config
        jsign_id = self.build_jsignature_id(name)
        jsignature_config = self.build_jsignature_config()

        # Prepare value
        value = self.prep_value(value)

        # Build output
        hidden_input = super(JSignatureWidget, self).render(name, value, attrs)
        div = u'<div id="%s" class="jsign-container"></div>' % jsign_id
        clr = u''
        if jsignature_config['ResetButton']:
            clr = u'<input type="button" value="%s" class="btn">' % _('Reset')
        js = u'$("#%s").jSignature(%s);' % (
            jsign_id, json.dumps(jsignature_config))
        js += u'$("#%s").jSignature("setData", %s,"native");' % (
            jsign_id, value)
        js = u'<script type="text/javascript">%s</script>' % js
        out = u'<div class="jsign-wrapper">%s%s%s%s</div>' % (
            hidden_input, div, clr, js)

        return mark_safe(out)
