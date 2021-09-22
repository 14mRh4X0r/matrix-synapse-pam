PAM auth provider for Synapse
=============================

Allows Synapse to use UNIX accounts through PAM.

Installation
------------

For Debian, packages are available on the `releases page`_.

For other distributions, install with ``./setup.py install``.

Usage
-----

Example Synapse config:

.. code:: yaml

    password_providers:
      - module: "pam_auth_provider.PAMAuthProvider"
        config:
          create_users: true
          skip_user_check: false

The ``create_users`` key specifies whether to create Matrix accounts
for valid system accounts.

The ``skip_user_check`` key can be used to skip verifying existence of the user
with NSS, in case PAM uses a different user database.

Copyright
---------

This software is copyright 2017, 2021 by Willem Mulder and licensed under the EUPL_.

.. _releases page: https://github.com/14mRh4X0r/matrix-synapse-pam/releases
.. _EUPL: https://joinup.ec.europa.eu/software/page/eupl
