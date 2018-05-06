#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.api.app
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

:var app: the Flask application object
:type app: :py:class:`modlit.api.Flask`
"""
# pylint: disable=invalid-name
from modlit.api import ModlitFlask

app: ModlitFlask = ModlitFlask(__name__.split('.')[0])  #: the Flask app itself
