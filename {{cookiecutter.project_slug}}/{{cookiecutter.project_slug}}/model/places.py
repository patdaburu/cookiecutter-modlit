#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.model.places
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>
"""
from sqlalchemy import Column, String
from geoalchemy2 import Geometry
from modlit.base import Base, ModelMixin, AutoIdMixin
from modlit.meta import column, ColumnMeta, Requirement, Source, Target, Usage
from modlit.model import model


@model(label='Places')
class Place(Base, ModelMixin, AutoIdMixin):
    """
    This is a sample ORM class with a point geometry that represents places.
    """

    __tablename__ = 'places'  #: the name of the database table

    geometry = Column(Geometry('POINT'))  #: the table geometry

    label = column(
        String,
        ColumnMeta(
            label='Label',
            description='a friendly label to describe the place',
            source=Source(requirement=Requirement.REQUIRED),
            target=Target(guaranteed=True,
                          usage=Usage.SEARCH | Usage.DISPLAY)
        )
    )
