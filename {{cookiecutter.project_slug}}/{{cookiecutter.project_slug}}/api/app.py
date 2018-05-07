#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.api.app
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

:var app: the Flask application object
:type app: :py:class:`flask.Flask`
"""
# pylint: disable=invalid-name
# pylint: disable=unused-import
from modlit.api import ModlitFlask

app: ModlitFlask = ModlitFlask(__name__.split('.')[0])  #: the Flask app itself

# Import the routes modules.  (This may look unconventional, but it is in-line
# with Flask's design.  Go to http://flask.pocoo.org/docs/1.0/patterns/packages/
# and read the section on "Circular Imports" for more information.)
import {{cookiecutter.project_slug}}.api.routes
