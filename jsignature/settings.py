from django.conf import settings

JSIGNATURE_WIDTH = getattr(
    settings, 'JSIGNATURE_WIDTH', 'ratio')
JSIGNATURE_HEIGHT = getattr(
    settings, 'JSIGNATURE_HEIGHT', 'ratio')
JSIGNATURE_COLOR = getattr(
    settings, 'JSIGNATURE_COLOR', '#000')
JSIGNATURE_BACKGROUND_COLOR = getattr(
    settings, 'JSIGNATURE_BACKGROUND_COLOR', '#FFF')
JSIGNATURE_DECOR_COLOR = getattr(
    settings, 'JSIGNATURE_DECOR_COLOR', '#DDD')
JSIGNATURE_LINE_WIDTH = getattr(
    settings, 'JSIGNATURE_LINE_WIDTH', 0)
JSIGNATURE_UNDO_BUTTON = getattr(
    settings, 'JSIGNATURE_UNDO_BUTTON', False)
JSIGNATURE_RESET_BUTTON = getattr(
    settings, 'JSIGNATURE_RESET_BUTTON', True)

JSIGNATURE_JQUERY = getattr(
    settings, 'JSIGNATURE_JQUERY', 'custom')

JSIGNATURE_DEFAULT_CONFIG = {
    'width': JSIGNATURE_WIDTH,
    'height': JSIGNATURE_HEIGHT,
    'color': JSIGNATURE_COLOR,
    'background-color': JSIGNATURE_BACKGROUND_COLOR,
    'decor-color': JSIGNATURE_DECOR_COLOR,
    'lineWidth': JSIGNATURE_LINE_WIDTH,
    'UndoButton': JSIGNATURE_UNDO_BUTTON,
    'ResetButton': JSIGNATURE_RESET_BUTTON,
}
