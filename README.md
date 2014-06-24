# django-taggit-autocomplete

This is a fork of django-tagging-autocomplete, which can be found at:
http://code.google.com/p/django-tagging-autocomplete/

It's virtually the same app, only it's changed to work with django-taggit:
http://github.com/alex/django-taggit

## Installation

   1. You need to have django-taggit already installed
   2. Download django-taggit-autocomplete and use setup.py to install it on your system:

      python setup.py install

   3. Download and install django-jquery-ui using
    pip install django-jquery-ui
   5. Add "taggit_autocomplete" to installed apps in your project's settings.
   6. Add the following line to your project's urls.py file:

    url(r'^taggit_autocomplete/', include('taggit_autocomplete.urls')),

   7. Include jquery-ui into the templates that will be using the field (see django-jquery-ui docs for details, it's not hard.)

## Usage

You can use TaggableManager to enable autocompletion right in your models.py file. In most cases this is the easiest solution. Example:

    from django.db import models
    from taggit_autocomplete.managers import TaggableManager

    class SomeModel(models.Model):
        tags = TaggableManager()
