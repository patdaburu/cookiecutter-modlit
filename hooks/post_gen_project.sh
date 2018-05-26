#!/usr/bin/env bash
make venv && source venv/bin/activate && make install && make build

echo -e "\033[1m\033[4mNext Steps\033[0m"
echo -e "\033[94mcd {{cookiecutter.project_slug}}\033[0m"
echo -e "\033[94msource venv/bin/activate\033[0m"
echo -e "\033[94m{{cookiecutter.project_slug}} --help\033[0m"


