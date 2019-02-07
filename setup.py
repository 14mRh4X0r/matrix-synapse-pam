#!/usr/bin/env python

# Copyright 2017 Willem Mulder
#
# Licensed under the EUPL, Version 1.1 or - as soon they will be approved by
# the European Commission - subsequent versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/software/page/eupl
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Licence is distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and
# limitations under the Licence.

from setuptools import setup

setup(
        name="matrix-synapse-pam",
        version="0.1.3",
        py_modules=['pam_auth_provider'],

        include_package_data = True,
        data_files = [("share/matrix-synapse-pam/expect", ["expect-su.expect"])],

        install_requires=[
            "Twisted>=8.0.0",
            "python-pam"
        ],

        author="Willem Mulder",
        author_email="willemmaster@hotmail.com",
        description="A PAM/UNIX auth provider for Synapse",
        url="https://github.com/14mRh4X0r/matrix-synapse-pam",
        license="EUPL"
)
