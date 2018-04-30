#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.api
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>
"""
from flask import Flask

app = Flask('{{cookiecutter.project_slug}}')  #: the Flask app itself