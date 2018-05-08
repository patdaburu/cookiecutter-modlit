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
from modlit.db import exec_sql


def preload(engine: Engine):
    """
    Call this function before loading the model to make sure the database is
    set up properly.

    :param engine: the engine connected to the database
    
    .. note::
    
        The function will run the SQL commands in the 
        {{cookiecutter.project_slug}}/db/preload.sql file.
    """
    preload_sql_file = Path(__file__).resolve().parent / 'preload.sql'
    exec_sql(engine, preload_sql_file)



