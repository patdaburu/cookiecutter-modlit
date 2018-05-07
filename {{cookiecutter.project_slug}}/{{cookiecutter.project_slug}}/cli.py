#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.model
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This is the entry point for the command-line interface (CLI) application.

.. note::

    To learn more about Click visit the
    `project website <http://click.pocoo.org/5/>`_.  There is also a very
    helpful `tutorial video <https://www.youtube.com/watch?v=kNke39OZ2k0>`_.
"""

import click
import modlit.model
from modlit.base import Base
from sqlalchemy import create_engine
from . import model
from .api.app import app


class Context(object):
    """
    This is an information object that can be used to pass data between CLI
    functions.
    """
    def __init__(self):  # Note that this object must have an empty constructor.
        self.debug: bool = False


# contextual is a decorator for functions that pass 'Context' objects.
contextual = click.make_pass_decorator(Context, ensure=True)  #: pylint: disable=invalid-name


@click.group()
@click.option('--debug', is_flag=True, help="enables debugging")
@contextual
def cli(context: Context, debug: bool):
    """
    This is the command line application for the {{cookiecutter.project_slug}}
    project.
    """
    context.debug = debug


@cli.command()
@click.option('-h', '--host', default='127.0.0.1', help="the listening host")
@click.option('-p', '--port', type=int, default=5000, help="the listening port")
@click.option('-d', '--db',
              default='postgresql://postgres:postgres@localhost/postgres',
              help='the database URL')
@click.option('--create', is_flag=True,
              help="create the model in the database")
@contextual
def run(context: Context, host: str, port: int, db: str, create: bool):
    """
    Run the REST API service.

    :param context: the command-line run context
    :param host: the listening host
    :param port: the listening port
    :param db: the URL of the database
    :param create: create the model in the database
    """
    # Create the engine.
    engine = create_engine(db)
    # Load the model.
    modlit.model.load(model)
    # If the caller indicated that we should, create the database tables.
    if create:
        Base.metadata.create_all(engine)
    # Share the engine for the application.
    app.install_engine(engine)
    # Run the Flask app.
    app.run(debug=context.debug,
            host=host,
            port=port)
