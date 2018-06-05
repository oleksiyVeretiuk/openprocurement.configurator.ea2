import unittest
from zope.component import getGlobalSiteManager
from openprocurement.api.interfaces import IProjectConfigurator
from openprocurement.api.configurator import Configurator

from openprocurement.configurator.ea2.includeme import includeme


class TestConfiguratorCreation(unittest.TestCase):

    def test_includeme(self):
        includeme()
        gsm = getGlobalSiteManager()
        configurator = gsm.queryUtility(IProjectConfigurator)

        self.assertIsNotNone(configurator)
        self.assertTrue(isinstance(configurator, Configurator))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConfiguratorCreation))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
