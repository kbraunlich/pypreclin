#! /usr/bin/env python
##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# pyConnectomist current version
version_major = 1
version_minor = 0
version_micro = 0

# Expected by setup.py: string of form "X.Y.Z"
__version__ = "{0}.{1}.{2}".format(version_major, version_minor, version_micro)

# Define default SPM STANDALONE path for the package
DEFAULT_SPM_STANDALONE_PATH = "/i2bm/local/bin/spm12"

# Define default FSL configuration path for the package
DEFAULT_FSL_PATH = "/etc/fsl/4.1/fsl.sh"

# Expected by setup.py: the status of the project
CLASSIFIERS = ["Development Status :: 5 - Production/Stable",
               "Environment :: Console",
               "Environment :: X11 Applications :: Qt",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering",
               "Topic :: Utilities"]

# Project descriptions
description = """
[pyPreClin]
This package provides common scripts:

* 
"""
long_description = """
=========
pyPreClin
=========

A Python project that provides a collection of python scripts for
preprocessing MRI preclinical data.
"""

# Main setup parameters
NAME = "pyPreClin"
ORGANISATION = "CEA"
MAINTAINER = "Antoine Grigis"
MAINTAINER_EMAIL = "antoine.grigis@cea.fr"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://bioproj.extra.cea.fr/"
DOWNLOAD_URL = "https://bioproj.extra.cea.fr/"
LICENSE = "CeCILL-B"
CLASSIFIERS = CLASSIFIERS
AUTHOR = "pyPreClin developers"
AUTHOR_EMAIL = "antoine.grigis@cea.fr"
PLATFORMS = "OS Independent"
ISRELEASE = True
VERSION = __version__
PROVIDES = ["pypreclin"]
REQUIRES = [
    "pypreprocess"]
EXTRA_REQUIRES = {}