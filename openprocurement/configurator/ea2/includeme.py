from zope.component import getGlobalSiteManager

from openprocurement.api.interfaces import IProjectConfigurator
from openprocurement.api.configurator import Configurator

config = {
    'AUCTION_PREFIX': 'UA-PS',
    'ASSET_PREFIX': 'UA-AR-P'
}

def includeme(*args, **kwargs):
    getGlobalSiteManager().registerUtility(Configurator(config, {}), IProjectConfigurator)
