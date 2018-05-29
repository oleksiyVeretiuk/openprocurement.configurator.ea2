import unittest
from zope.component import getGlobalSiteManager
from openprocurement.api.interfaces import IProjectConfigurator
from openprocurement.api.configurator import Configurator

from includeme import includeme


class TestConfiguratorCreation(unittest.TestCase):

    def test_includeme(self):
        includeme()
        gsm = getGlobalSiteManager()
        configurator = gsm.queryUtility(IProjectConfigurator)

        assert configurator is not None
        assert isinstance(configurator, Configurator) is True


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConfiguratorCreation))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
