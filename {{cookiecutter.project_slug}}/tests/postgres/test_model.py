#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.model.places
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This module contains tests that evaluate the model against a temporary
Postgres database.
"""

import unittest
from {{cookiecutter.project_slug}}.db import lifecycle
from modlit.testing.postgres import TempDatabase


class ExampleTestSuite(unittest.TestCase):
    """
    This test suite evaluates the model against a Postgres database.
    """
    def test_createTempDb_load_noErrors(self):
        """
        Arrange: Create a temporary database.
        Act: Load the data model.
        Assert: No errors occurred.
        """
        with TempDatabase() as tempdb:
            lifecycle.load(tempdb.engine, create=True)
            # If no exceptions occur, the creation of the data model was
            # complete and successful.
            self.assertEqual(True, True)
