# -*- coding: utf-8 -*-
"""
Templates for all files this extension provides
"""
from pkg_resources import resource_string

import os
import string


def get_template(name):
    """Retrieve the template by name
    Args:
        name: name of template
    Returns:
        :obj:`string.Template`: template
    """
    file_name = "{name}.template".format(name=name)
    data = resource_string(__name__, file_name)
    # we assure that line endings are converted to '\n' for all OS
    data = data.decode(encoding="utf-8").replace(os.linesep, "\n")
    return string.Template(data)


def noxfile(opts):
    """Template for noxfile.py

    Args:
        opts (dict): Missing parameters
    Returns:
        str (str): File content as string
    """
    template = get_template("noxfile")
    return template.substitute(opts)
