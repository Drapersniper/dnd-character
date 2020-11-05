"""
dnd-character is a Python package for integrating DnD characters
into external applications.
"""


__author__ = "Brianna Rainey"
__copyright__ = "Copyright 2019-2020 Brianna Rainey & Markis Cook"
__credits__ = ["Brianna Rainey (Current Programmer)", "Markis Cook (Original Creator)"]
__license__ = "EPL-2.0"
__version__ = "20.11.04"
__maintainer__ = "Brianna Rainey"


from .character import Character as CharacterObj
from .classes import *


def Character(**kwargs):
    """
    Factory function for a new Character
    """
    new = CharacterObj(**kwargs)
    if "experience" in kwargs:
        new.experience = kwargs["experience"]
        new._level = kwargs.get("level", new._level)
    return new
