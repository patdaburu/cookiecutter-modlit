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
import sqlparse


def preload(engine: Engine):
    """
    Call this function before loading the model to make sure the database is
    set up properly.

    :param engine: the engine connected to the database
    """
    preload_sql_file = Path(__file__).resolve().parent / 'preload.sql'
    with engine.connect() as connection:
        for sql_stmt in sqlparse.split(preload_sql_file.read_text().strip()):
            connection.execute(sql_stmt)


