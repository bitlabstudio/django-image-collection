Django Image Collection
=======================

A reusable Django app to organise images in collections and output them in sliders or galleries by simply adding a template tag.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-image-collection

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-image-collection.git#egg=image_collection

TODO: Describe further installation steps (edit / remove the examples below):

Add ``image_collection`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'image_collection',
        'generic_positions',
    )

Add the ``image_collection`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^image-collection/', include('image_collection.urls')),
        url(r'^pos/', include('generic_positions.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load image_collection_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate image_collection
    ./manage.py migrate generic_positions


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-image-collection
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.
