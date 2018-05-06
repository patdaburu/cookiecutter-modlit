#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: {{cookiecutter.project_slug}}.api.routes.info
.. moduleauthor:: {{cookiecutter.author_name}} <{{cookiecutter.author_email}}>
"""
from flask import jsonify
import modlit_template as package
from ..app import app


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
