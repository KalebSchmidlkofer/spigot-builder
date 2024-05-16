from .util import *

def loadPlugin(project:str) -> list:
  paperVersions  = get_papermc_versions(project=project)
  return paperVersions


def loadVanilla() -> list:
  baseVersions   = get_vanilla_version()
  return baseVersions
