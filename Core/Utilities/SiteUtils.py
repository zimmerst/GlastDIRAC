""" Site Utils package, for doing some nasty calls
@author: S. Zimmer (OKC)
"""
from DIRAC                                              import gLogger, S_OK, S_ERROR
from DIRAC.Core.Base.DB                                 import DB
from DIRAC.ConfigurationSystem.Client.Helpers.Resources import getQueues
from DIRAC.ConfigurationSystem.Client.Helpers.Registry  import getVO


def getSiteForCE(ces):
    """ We want to get the site for a given CE because that's what the job expects
    """
    #!FIXME! remove dependency on glast.org
    vo = getVO("glast.org")
    res = getQueues(community = vo)
    if not res['OK']:
        return S_ERROR("Could not get site for CE")
    sitedict = res['Value']
    final_sdict = {}
    for site, s_ces in sitedict.items():
        for ce in ces:
            if ce in s_ces:
                if not site in final_sdict:
                    final_sdict[site] = []
                final_sdict[site].append(ce)
    
    return S_OK(final_sdict)

