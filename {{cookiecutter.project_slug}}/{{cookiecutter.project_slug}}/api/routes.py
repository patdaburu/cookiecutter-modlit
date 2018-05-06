#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.api.routes
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>

This module contains the Flask app definition for the project.
"""
from flask import jsonify
from geoalchemy2 import functions
import {{cookiecutter.project_slug}} as package
from .app import app
from ..model.places import Place


# https://www.youtube.com/watch?v=WxGBoY5iNXY&t=817s


@app.route('/info', methods=['GET'])
def get_info():
    """
    Get general information about the running API.

    :return: information about the running API
    """
    return jsonify({
        'package': package.__name__,
        'version': package.__version__,
        'release': package.__release__
    })


@app.route('/places', methods=['GET'])
def get_places():
    """

    :return:
    """
    session = app.session()
    places = session.query(
        Place.id,
        Place.label,
        functions.ST_AsGeoJSON(Place.geometry).label('geometry')
    )
    output = []
    for place in places:
        place_data = {
            'id': place.id,
            'label': place.label,
            'geometry': place.geometry
        }
        output.append(place_data)
    session.close()
    return jsonify({'places': output})