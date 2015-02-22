SublimeLinter-contrib-glslangValidator
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-glslangValidator.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-glslangValidator)  

This linter plugin for [SublimeLinter][docs] provides an interface to [glslangValidator](https://github.com/numb3r23/SublimeLinter-contrib-glsl). It will be used with files that have the “glsl” and "essl" syntax provided by the SublimeText plugin [OpenGL Shading Language (GLSL)](https://github.com/euler0/sublime-glsl). It allows you to compile the shader code for a single shader using the Kronos Reference-Compiler and view the errors as annotations to your code without having to create an OpenGL context.

## tl;dr
1. Install  
    - **glslangValidator** in **path**
    - **SublimeLinter 3** plugin
    - **this plugin**
2. Use correct **file-extension**(.vert, .frag, ...)

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `glslangValidator` is installed on your system. To install `glslangValidator`, do the following:

1. Got to [Kronos GLSL Reference-Compiler](https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/).
    1. Either pick a *binary* to install (currently provided for Windows & Linux) or
    2. Download the source and compile & install it (currently only option for OSX - but no worries, it comes with CMake and worked out of the box for me)
2. Ensure it's in your path, e.g. ```glslangValidator``` in a terminal produces not an error.

### Linter configuration
In order for `glslangValidator` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `glslangValidator`, you can proceed to install the SublimeLinter-contrib-glslangValidator plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `glslangValidator`. Among the entries you should see `SublimeLinter-contrib-glslangValidator`. If that entry is not highlighted, use the keyboard or mouse to select it.

## glslangValidator specifics
1. Currently only **error**-messages are parsed. If somebody has a good example I'm more than willing to add it.
2. Use the appropriate file-extension glslangValidator expects:
    - ```.vert``` for a **vertex** shader
    - ```.tesc``` for a **tessellation control** shader
    - ```.tese``` for a **tessellation evaluation** shader
    - ```.geom``` for a **geometry** shader
    - ```.frag``` for a **fragment** shader
    - ```.comp``` for a **compute** shader

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
