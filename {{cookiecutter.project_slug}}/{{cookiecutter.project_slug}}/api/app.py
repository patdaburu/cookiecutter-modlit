#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.api.app
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

:var app: the Flask application object
:type app: :py:class:`flask.Flask`
:var engine: the SQLAlchemy engine
:type engine: :py:class:`sqlalchemy.engine.base.Engine`
"""
# pylint: disable=invalid-name
from flask import Flask
from sqlalchemy.engine.base import Engine
from typing import Any, Dict

__shared__: Dict[str, Any] = {}  #: a dictionary of shared values

app: Flask = Flask('{{cookiecutter.project_slug}}')


def get_engine() -> Engine:
    """
    Get the SQLAlchemy engine for the application.

    :return: the SQLAlchemy engine
    """
    return __shared__['__engine__']


def install_engine(engine: Engine):
    """
    Install the SQLAlchemy engine for the application.

    :param engine: the engine
    """
    __shared__['__engine__'] = engine