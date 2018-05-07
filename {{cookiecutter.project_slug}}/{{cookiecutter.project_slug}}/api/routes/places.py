#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
.. currentmodule:: {{cookiecutter.project_slug}}.api.routes.info
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>
"""
from flask import jsonify
from geoalchemy2 import functions
from ..app import app
from ...model.places import Place


@app.route('/places', methods=['GET'])
def get_places():

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


@app.route('/places/<id>', methods=['GET'])
def get_place(id_):

    session = app.session()
    place = session.query(
        Place.id,
        Place.label,
        functions.ST_AsGeoJSON(Place.geometry).label('geometry')
    ).filter_by(id=id_).first()
    if not place:
        return jsonify({'message': 'No user found.'})

    place_data = {
        'id': place.id,
        'label': place.label,
        'geometry': place.geometry
    }
    session.close()
    return jsonify(place_data)