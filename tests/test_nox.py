import sys
from os.path import exists as path_exists

from pyscaffold.api import create_project
from pyscaffold.cli import run

from pyscaffoldext.nox.extension import Nox


def test_create_project_with_nox(tmpfolder):
    "Test create_project with nox extension"
    # Options with nox extension
    opts = dict(project="proj", extensions=[Nox("nox")])

    # create project
    create_project(opts)

    # test if noxfile created
    assert path_exists("proj/noxfile.py")


def test_create_project_without_nox(tmpfolder):
    "Test create_project without nox extension"
    # Options without nox extension
    opts = dict(project="proj")

    # create project
    create_project(opts)

    # make sure that noxfile is not created
    assert not path_exists("proj/noxfile.py")


def test_cli_with_nox(tmpfolder):
    "Test commandline project creation with nox extension"
    # give nox extension
    sys.argv = ["pyscaffold", "--nox", "proj"]

    # create project
    run()

    # noxfile should exist
    assert path_exists("proj/noxfile.py")


def test_cli_without_nox(tmpfolder):
    "Test commandline project creation without nox extension"
    # give nox extension
    sys.argv = ["pyscaffold", "proj"]

    # create project
    run()

    # noxfile should exist
    assert not path_exists("proj/noxfile.py")
