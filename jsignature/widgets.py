"""
    Provides a django form widget to handle a signature capture field with
    with jSignature jQuery plugin
"""
import json

from django.conf import settings
from django.template.loader import render_to_string
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from jsignature.settings import JSIGNATURE_DEFAULT_CONFIG

JSIGNATURE_EMPTY_VALUES = validators.EMPTY_VALUES + ('[]', )


try:
    from django.utils import six
    string_types = six.string_types
except ImportError:
    string_types = str


class JSignatureWidget(forms.HiddenInput):
    """
    A widget handling a signature capture field with with jSignature
    """

    # Actually, this widget has a display so we want it to behave like a
    # normal field, not a hidden one
    is_hidden = False

    @property
    def media(self):
        JSIGNATURE_JQUERY = getattr(settings, 'JSIGNATURE_JQUERY', 'custom')
        files = ()
        if JSIGNATURE_JQUERY == 'admin':
            files = (
                'admin/js/jquery.init.js',
                'js/jsignature_admin_init.js',
            )
        elif JSIGNATURE_JQUERY != 'custom':
            files = (JSIGNATURE_JQUERY,)
        files += (
            'js/jSignature.min.js',
            'js/django_jsignature.js',
        )
        return forms.Media(js=files)

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
        elif isinstance(value, string_types):
            return value
        elif isinstance(value, list):
            return json.dumps(value)
        raise ValidationError('Invalid format.')

    def render(self, name, value, attrs=None, renderer=None):
        """ Render widget """
        # Build config
        jsign_id = self.build_jsignature_id(name)
        jsignature_config = self.build_jsignature_config()

        # Prepare value
        value = self.prep_value(value)

        # Build output
        context = {
            'hidden': super(JSignatureWidget, self).render(name, value, attrs),
            'jsign_id': jsign_id,
            'reset_btn_text': _('Reset'),
            'config': jsignature_config,
            'js_config': mark_safe(json.dumps(jsignature_config)),
            'value': mark_safe(value),
        }
        out = render_to_string('jsignature/widget.html', context)

        return mark_safe(out)
