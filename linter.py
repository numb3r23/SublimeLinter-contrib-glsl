#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#
# ******
#
# GLSLLint interface to glslangValidator written by numb3r23

"""This module exports the GLSLLint plugin linter class."""

from SublimeLinter.lint import Linter, util


class GLSLLint(Linter):

    """Provides an interface to glslangValidator."""

    syntax = ('glsl', 'essl')
    cmd = ('glslangValidator', '@')
    regex = (r'^ERROR:\s.*:(?P<line>\d+):\s\'(?P<near>.*)\'\s:\s+(?P<message>.+)')
    error_stream = util.STREAM_BOTH
    tempfile_suffix = '-'
