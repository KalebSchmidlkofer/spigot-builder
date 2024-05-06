from .util import *

def loadPlugin() -> list:
  paperVersions  = get_paper_versions()
  return paperVersions


def loadVanilla() -> list:
  baseVersions   = get_vanilla_version()
  return baseVersions