#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: pre_gen_project
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This is the script that runs after template generation is complete.
"""
# These are the colors we may use as we print messages for the user.
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

print(HEADER + 'Next Steps:' + ENDC)
print('cd {{cookiecutter.project_slug}}')
print('make venv')
