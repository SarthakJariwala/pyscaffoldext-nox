# -*- coding: utf-8 -*-
"""Implementation to add noxfile.py to
PyScaffold project
"""
from pathlib import PurePath

from pyscaffold.api import Extension, helpers

from .templates import noxfile


class Nox(Extension):
    """
    Generate Nox configuration file for PyScaffold
    """

    def activate(self, actions):
        """Activate extension

        Args:
            actions (list): list of actions to perform

        Returns:
            list: updated list of actions
        """
        actions = self.register(actions, self.add_noxfile, after="define_structure")
        return actions

    def add_noxfile(self, struct, opts):
        """Add a noxfile.py file

        Args:
            struct (dict): project representation as (possibly) nested
                :obj:`dict`.
            opts (dict): given options, see :obj:`create_project` for
                an extensive list.

        Returns:
            struct, opts: updated project representation and options
        """
        files = PurePath(opts["project"], "noxfile.py")
        content = noxfile(opts)
        struct = helpers.ensure(struct, files, content, helpers.NO_OVERWRITE)
        return struct, opts
