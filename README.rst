A simple way to use `jSignature jQuery plugin <https://github.com/brinley/jSignature/blob/master/README.md>`_ in your `Django <https://www.djangoproject.com>`_ projects.

It provides:

* A form field and a form widget to handle jquery plugin through a Django form;
* A model field to store a captured signature;
* A mixin adding two fields (signature / signature_date) in any of your Django models.
* A template filter to render signatures as base64 image urls.

.. image:: https://img.shields.io/pypi/v/django-jsignature.svg
    :target: https://pypi.python.org/pypi/django-jsignature/
    :alt: Latest PyPI version

.. image:: https://github.com/fle/django-jsignature/actions/workflows/actions.yml/badge.svg
    :target: https://github.com/fle/django-jsignature/actions
    :alt: Build status

.. image:: https://coveralls.io/repos/github/fle/django-jsignature/badge.svg?branch=master
    :target: https://coveralls.io/github/fle/django-jsignature?branch=master
    :alt: Coverage status

.. image:: https://github.com/fle/django-jsignature/blob/master/screen.png

==================
Installation
==================

::

    pip install django-jsignature

==================
Usage
==================

* Add ``jsignature`` to your ``INSTALLED_APPS``:

.. code-block:: python

    # settings.py
    INSTALLED_APPS = (
        ...
        'jsignature',
    )

* Use provided model field (for easy storage):

.. code-block:: python

    # models.py
    from django.db import models
    from jsignature.fields import JSignatureField

    class SignatureModel(models.Model):
        signature = JSignatureField()

* In your form template

.. code-block:: html+django

    {{ form.media }}
    <form action="" method="post">
        {{ form }}
        <input type="submit" value="Save" />
        {% csrf_token %}
    </form>

* Render image from db value in your display template:

.. code-block:: html+django

    {# yourtemplate.html #}
    {% load jsignature_filters %}

    <img src="{{ obj.signature|signature_base64 }}" alt="{{ obj }}" />


*   By default, jSignature is made to work outside of admin, requiring that
    you include the jQuery library in your ``<head>``.

    If you want to use jSignature in the Django admin site, set the
    ``JSIGNATURE_JQUERY`` setting to ``admin``. Otherwise if set to any url
    pointing to jQuery, it will be automatically included.

    It is strongly suggested to take example from ``example_project``, which is
    `located in this repo <https://github.com/fle/django-jsignature/tree/master/example_project>`_

==================
Customization
==================

JSignature plugin options are available in python:

* Globally, in your settings:

.. code-block:: python

    # settings.py
    JSIGNATURE_WIDTH = 500
    JSIGNATURE_HEIGHT = 200

* Specifically, in your form:

.. code-block:: python

    # forms.py
    from jsignature.forms import JSignatureField
    from jsignature.widgets import JSignatureWidget

    JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

Available settings are:

* ``JSIGNATURE_WIDTH`` (width)
* ``JSIGNATURE_HEIGHT`` (height)
* ``JSIGNATURE_COLOR`` (color)
* ``JSIGNATURE_BACKGROUND_COLOR`` (background-color)
* ``JSIGNATURE_DECOR_COLOR`` (decor-color)
* ``JSIGNATURE_LINE_WIDTH`` (lineWidth)
* ``JSIGNATURE_UNDO_BUTTON`` (UndoButton)
* ``JSIGNATURE_RESET_BUTTON`` (ResetButton)

==================
In your models
==================

If you want to store signatures easily, a provided mixin gives a ``signature``
and a ``signature_date`` that update themselves:

.. code-block:: python

    from django.db import models
    from jsignature.mixins import JSignatureFieldsMixin

    class JSignatureModel(JSignatureFieldsMixin):
        name = models.CharField()


==================
In your forms
==================

* If you need more precise handling of the form field, you can use it directly:

.. code-block:: python

    # forms.py
    from django import forms
    from jsignature.forms import JSignatureField

    class SignatureForm(forms.Form):
        signature = JSignatureField()


* And upon saving, have direct access to the image with ``draw_signature()``

.. code-block:: python

    # views.py
    from jsignature.utils import draw_signature
    from myapp.forms import SignatureForm

    def my_view(request):
        form = SignatureForm(request.POST or None)
        if form.is_valid():
            signature = form.cleaned_data.get('signature')
            if signature:
                # as an image
                signature_picture = draw_signature(signature)
                # or as a file
                signature_file_path = draw_signature(signature, as_file=True)


==================
Example project
==================

If you want to have a demo of this package, just use the example project:

.. code-block:: shell

    git clone https://github.com/fle/django-jsignature.git
    cd django-jsignature
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -e .
    cd example_project
    ./manage.py migrate
    ./manage.py createsuperuser

Fill the user info, launch django with ``./manage.py runserver`` and head over
to `http://127.0.0.1:8000/ <http://127.0.0.1:8000/>`_, you can also
`login to the admin <http://127.0.0.1:8000/admin>`_ with the credentials your
provided.

==================
Authors
==================

    * Florent Lebreton <florent.lebreton@makina-corpus.com> (original author)
    * Sébastien Corbin <sebastien.corbin@makina-corpus.com> (maintainer)

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com

