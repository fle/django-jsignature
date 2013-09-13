"""
    Provides a django form widget to handle a signature capture field with
    with jSignature jQuery plugin
"""
import json
from django.forms.widgets import HiddenInput
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from jsignature.settings import JSIGNATURE_DEFAULT_CONFIG

class JSignatureWidget(HiddenInput):
    """
    A widget handling a signature capture field with with jSignature
    """

    class Media:
        js = ('js/jSignature.min.js',
              'js/django_jsignature.js')

    def __init__(self, attrs=None, jsignature_attrs=None):
        super(JSignatureWidget, self).__init__(attrs)
        # Store jSignature js config
        self.jsignature_attrs = jsignature_attrs or {}

    def render(self, name, value, attrs=None):

        # Build config
        jsign_id = 'jsign_%s' % name
        jsignature_config = JSIGNATURE_DEFAULT_CONFIG.copy()
        jsignature_config.update(self.jsignature_attrs)

        # Build output
        hidden_input = super(JSignatureWidget, self).render(name, value, attrs)
        div = u'<div id="%s" class="jsign-container"></div>' % jsign_id
        clr = u'<input type="button" value="%s" class="btn">' % _('Reset')
        js  = u'$("#%s").jSignature(%s);' % (jsign_id, json.dumps(jsignature_config))
        js += u'$("#%s").jSignature("setData", %s,"native");' % (jsign_id, json.dumps(value))
        js  = u'<script type="text/javascript">%s</script>' % js
        out = u'<div class="jsign-wrapper">%s%s%s%s</div>' % (hidden_input, div, clr, js)

        return mark_safe(out)
