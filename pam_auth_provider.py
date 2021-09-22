# Copyright 2017, 2021 Willem Mulder
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

import pam
import pwd

from collections import namedtuple
from twisted.internet import defer

class PAMAuthProvider:
    def __init__(self, config, account_handler):
        self.account_handler = account_handler
        self.create_users = config.create_users
        self.skip_user_check = config.skip_user_check

    @defer.inlineCallbacks
    def check_password(self, user_id, password):
        """ Attempt to authenticate a user against PAM
            and register an account if none exists.

            Returns:
                True if authentication against PAM was successful
        """
        if not password:
            defer.returnValue(False)
        # user_id is of the form @foo:bar.com
        localpart = user_id.split(":", 1)[0][1:]

        # check whether user even exists
        if not self.skip_user_check:
            try:
                pwd.getpwnam(localpart)
            except KeyError:
                defer.returnValue(False)

        # Now check the password
        if not pam.pam().authenticate(localpart, password, service='matrix-synapse'):
            defer.returnValue(False)

        # From here on, the user is authenticated

        # Create the user in Matrix if it doesn't exist yet
        if not (yield self.account_handler.check_user_exists(user_id)):
            # Bail if we don't want to create users in Matrix
            if not self.create_users:
                defer.returnValue(False)

            yield self.account_handler.register(localpart=localpart)

        defer.returnValue(True)

    @staticmethod
    def parse_config(config):
        pam_config = namedtuple('_Config', 'create_users')
        pam_config.create_users = config.get('create_users', True)
        pam_config.skip_user_check = config.get('skip_user_check', False)

        return pam_config
