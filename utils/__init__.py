from .util import *
from .calls import *
def loadPlugin(project:str) -> list:
  paperVersions  = get_papermc_versions(project=project)
  return paperVersions

def loadPurpur(project:str) -> list:
  purpurVersions = get_purpur_versions(project=project)
  return purpurVersions

def loadVanilla() -> list:
  baseVersions   = get_vanilla_version()
  return baseVersions
