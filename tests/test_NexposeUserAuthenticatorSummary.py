# Future Imports for py2/3 backwards compat.
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .load_unittest import unittest
from .LoadFixture import CreateEmptyFixture, LoadFixture, XML
from nexpose.nexpose_userauthenticator import UserAuthenticatorSummary
from future import standard_library
standard_library.install_aliases()


class NexposeUserAuthenticatorSummaryTestCase(unittest.TestCase):
    def testCreateFromXML(self):
        fixture = CreateEmptyFixture(XML)
        authenticator = UserAuthenticatorSummary.CreateFromXML(fixture)
        self.assertEquals(0, authenticator.id)
        self.assertEquals('', authenticator.source)
        self.assertEquals('', authenticator.module)
        self.assertEquals(False, authenticator.is_external)

        fixture = LoadFixture('UserAuthenticatorListingResponse.xml')

        authenticator = UserAuthenticatorSummary.CreateFromXML(fixture[0])
        self.assertEquals(1, authenticator.id)
        self.assertEquals('Builtin Administrators', authenticator.source)
        self.assertEquals('XML', authenticator.module)
        self.assertEquals(False, authenticator.is_external)

        authenticator = UserAuthenticatorSummary.CreateFromXML(fixture[1])
        self.assertEquals(2, authenticator.id)
        self.assertEquals('Builtin Users', authenticator.source)
        self.assertEquals('DataStore', authenticator.module)
        self.assertEquals(False, authenticator.is_external)

        authenticator = UserAuthenticatorSummary.CreateFromXML(fixture[2])
        self.assertEquals(3, authenticator.id)
        self.assertEquals('My Users', authenticator.source)
        self.assertEquals('LDAP', authenticator.module)
        self.assertEquals(True, authenticator.is_external)
