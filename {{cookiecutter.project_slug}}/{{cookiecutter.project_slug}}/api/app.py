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
from modlit.api import ModlitFlask, load_routes
from . import routes

app: ModlitFlask = ModlitFlask(__name__.split('.')[0])  #: the Flask app itself

# Import the route modules.
load_routes(routes)
