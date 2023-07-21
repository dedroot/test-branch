#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---[Name & Creation/Update Dates]------------------------------------------ #
#  Filename ~ settings.py                    [ Created: 2023-07-21 | 10:03 ]  #
#                                            [ Updated: 2023-07-21 | 10:10 ]  #
# ---[Description & File Language]------------------------------------------- #
#  Settings file of GitPy                                                     #
#  Language ~ Python3                                                         #
#  Version ~ 1.0.0                                                            #
# ---[Authors]--------------------------------------------------------------- #
#  Thomas Pellissier (MyMeepSQL)                                              #
# ---[Maintainer]------------------------------------------------------------ #
#  Thomas Pellissier (MyMeepSQL)                                              #
# ---[Operating System]------------------------------------------------------ #
#  Developed for Linux distros (for Debian and Arch based, for the moment)    #
# --------------------------------------------------------------------------- #


"""
This module is used to store the settings of GitPy.
"""


import sys

# Versions
LOCAL_VERSION = "1.1.0"
ONLINE_VERSION = "1.1.0"
PYTHON_VERSION = sys.version

# GitPy's owners
OWNER_FULLNAME = "Thomas Pellissier"
OWNER_CODENAME = "MyMeepSQL"
OWNER_DISCORD = "mymeepsql"
OWNER_EMAIL = "thomas.pellissier.pro@proton.me"
OWNER_GITHUB = "https://github.com/MyMeepSQL"
OWNER_TWITTER = "https://twitter.com/MyMeepSQL"

# GitPy's repository information
REPO_LICENSE_NAME = "GPL-3.0"
REPO_LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"
REPO_TYPE = "git"
REPO_PROVIDER = "GitHub"
REPO_URL = "https://github.com/MyMeepSQL/gitpy"
REPO_CLONE_URL = "https://github.com/MyMeepSQL/gitpy.git"
REPO_CHANGELOG_URL = "https://github.com/MyMeepSQL/gitpy/blob/master/CHANGELOG.md"
REPO_ISSUES_URL = "https://github.com/MyMeepSQL/gitpy/issues"
# METADATA_URL_FROM_MASTER = (
#     "https://github.com/MyMeepSQL/gitpy/blob/master/gitpy/src/configs/metadata.yml"
# )
# METADATA_URL_FROM_DEVELOP = (
#     "https://github.com/MyMeepSQL/gitpy/blob/develop/gitpy/src/configs/metadata.yml"
# )
MASTER_BRANCH = "master"
DEVELOP_BRANCH = "develop"

GITPY_BANNER = """{SB2}{bold}
        \r ┌─┐┬┌┬┐┌─┐┬ ┬ {W}{bold}{{W}{D}%s{W}{bold}}{W}{SB2}{bold}
        \r │ ┬│ │ ├─┘└┬┘ {W}{D}by MyMeepSQL{W}{SB2}{bold}
        \r └─┘┴ ┴ ┴   ┴  {W}{GR}{underscore}%s{W}""" % (
    LOCAL_VERSION,
    REPO_URL,
)

# Name of the tool
PROGRAM_NAME = "gitpy"
# Arguments variables
# Verbosity level: 1 = executed commands, 2 = executed commands and stdout/stderr,
# 3 = level 1 + 2 + more information about the execution of Python functions
VERBOSE = 0
# Prevent header from displaying
QUIET = False
# Skip the system update phase
SKIP_UPDATE = False
# install GitPy with the local files
OFFLINE_INSTALL = False
# Skip all "Are you sure?" questions
NON_CONFIRM = False
# Custom install Path
CUSTOM_INSTALL_PATH = None
# Force update GitPy
FORCE_UPDATE = False
# Remove GitPy' dependencies
REMOVE_DEPENDENCIES = False

# Path variables
# Working directory
CWD = "."
# Where GitPy is installed by default
DEFAULT_INSTALL_PATH = r"/opt/gitpy"
# The bin directory of GitPy
BIN_PATH = r"/usr/bin"
# The GitPy temporary directory
TEMP_PATH = r"/tmp/gitpy_tmpfolder"
# The GitPy config file
DEFAULT_GITPY_CONFIG_FILE_PATH = (
    "%s/gitpy/src/configs/gitpy_config.yml" % DEFAULT_INSTALL_PATH
)

# Environment variables
GITPY_PATH_ENV_VAR_NAME = "GITPY_INSTALL_PATH"
GITPY_PATH_ENV_VAR_VALUE = DEFAULT_INSTALL_PATH

# The version's messages for the version command
VERSION_MESSAGE = LOCAL_VERSION
VERSION_MESSAGE_VERBOSE2 = "%s %s\nPython %s" % (
    PROGRAM_NAME,
    LOCAL_VERSION,
    PYTHON_VERSION,
)
VERSION_MESSAGE_VERBOSE3 = """GitPy (GP) %s

\rCopyright (C) 2023 Thomas Pellissier.
\rLicense GPLv3+: GNU GPL version 3 or later
\r<http://www.gnu.org/licenses/gpl.html>.
\rThis is free software: you are free to change and redistribute it.
\rThere is NO WARRANTY, to the extent permitted by law.

\rOriginally written by Thomas Pellissier <%s>.
\rPlease send bug reports and questions to <%s>
\ror open an issue on <%s>.

\rPython version: Python %s""" % (
    LOCAL_VERSION,
    OWNER_EMAIL,
    OWNER_EMAIL,
    REPO_ISSUES_URL,
    PYTHON_VERSION,
)
