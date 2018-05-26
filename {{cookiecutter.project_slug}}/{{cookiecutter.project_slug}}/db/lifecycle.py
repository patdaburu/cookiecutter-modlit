#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.api.db.lifecycle
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This file contains functions that we might want to execute at various points
in our database's lifecycle.
"""
from pathlib import Path
from sqlalchemy.engine.base import Engine
from modlit.base import Base
from modlit.db.sqlalchemy import exec_sql
from modlit.db.postgres import touch_db
import modlit.model
from .. import model


def preload(engine: Engine):
    """
    Call this function before loading the model to make sure the database is
    set up properly.

    :param engine: the engine connected to the database

    .. note::

        The function will run the SQL commands in the
        {{cookiecutter.project_slug}}/db/preload.sql file.
    """
    touch_db(url=str(engine.url))
    preload_sql_file = Path(__file__).resolve().parent / 'preload.sql'
    exec_sql(engine, preload_sql_file)


def load(engine: Engine, create: bool):
    """
    Load the data `{{cookiecutter.project_slug}}` data model.

    :param engine: the engine that is connected to the database
    :param create: `true` if the loading process should include the creation
        of the physical database

    .. sealso::

        :py:func:`preload`, :py:func:`afterload`
    """
    # If we've been asked to create the physical database...
    if create:
        # ...perform the preload logic.
        preload(engine)
    # In any case, let's load the model package.
    modlit.model.load(model)
    # If we're creating physical structures...
    if create:
        # ...let SQLAlchemy do its thing.
        Base.metadata.create_all(engine)
        # Now perform any steps that need to occur afterward.
        afterload(engine)


def afterload(engine: Engine):
    """
    Call this function after loading the model to make whatever additional
    modifications you require.

    :param engine: the engine connected to the database

    .. note::

        The function will run the SQL commands in the
        {{cookiecutter.project_slug}}/db/afterload.sql file.
    """
    preload_sql_file = Path(__file__).resolve().parent / 'afterload.sql'
    exec_sql(engine, preload_sql_file)
