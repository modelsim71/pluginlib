# Copyright 2014 - 2018 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
**Left hook**
Test data standard library
"""

from tests.testdata.parents import Hook


class Left(Hook):
    """Dummy left hook"""

    _alias_ = 'left'

    def hook(self):
        """Throw hook"""
        return self._alias_
