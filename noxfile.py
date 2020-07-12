# -*- coding: utf-8 -*-
import os

import nox

travis_python_version = os.environ.get("TRAVIS_PYTHON_VERSION")
if travis_python_version:
    python = [travis_python_version]
else:
    python = ["3.5", "3.6", "3.7"]


@nox.session(python=python)
def tests(session):
    """Run tests"""
    # session.run("python", "setup.py", "install") # can't get coverage repory with this
    session.install(
        "-e",
        ".",
        "pytest",
        "pytest-cov",
        "pytest-virtualenv",
        "coverage",
        "coveralls",
        "flake8",
        "pre-commit",
    )
    session.run("pytest")


@nox.session
def blacken(session):
    """Run black code formatter"""
    session.install("black", "isort")
    files = ["src", "tests", "noxfile.py", "setup.py"]
    session.run("black", *files)
    session.run("isort", *files)


@nox.session
def docs(session):
    """Build docs"""
    session.install("sphinx")
    session.run("python", "setup.py", "docs")
