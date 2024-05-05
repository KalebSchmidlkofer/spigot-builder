from .util import *

def loadPlugin():
  paperVersions  = get_paper_versions()
  return paperVersions


def loadVanilla():
  baseVersions   = get_vanilla_version()
  return baseVersions