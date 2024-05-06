import requests
from loguru import logger
from pydantic import BaseModel
from sys import stderr
from typing import Optional

class softwaretypes(BaseModel):
  paper: str
  purpur: str
  spigot: str
  vanilla: str
  CraftBukkit: str
  Tuinity: str
  Airplane: str
  Folia: str
  SpongeVanila:str
  Glowstone:str
  Fabric:str
  Forge:str
  Crucible:str
  Cardboard:str
  Arclight:str
  Mohist:str
  Magma:str
  SpongeForge:str
  Quilt:str
  Banner:str
  MohistNeo:str
  Waterfall:str
  Velocity:str
  Bungeecord:str
  Travertine:str


def load_logging(trace, logfile:Optional[str]=None):
  logger.remove()
  if not logfile == None:
    logger.add(logfile, backtrace=True, diagnose=True)
  if trace:
    logger.add(stderr, level='TRACE')
  else:
    logger.add(stderr, level='INFO')


papermc_api='https://api.papermc.io/v2/projects/'

def get_paper_versions():
  vapi=f'{papermc_api}/paper'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions

def get_folia_versions():
  vapi=f'{papermc_api}/folia'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions

def get_velocity_versions():
  vapi=f'{papermc_api}/folia'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions

def get_waterfall_versions():
  vapi=f'{papermc_api}/folia'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions




def get_vanilla_version():
  vapi='https://launchermeta.mojang.com/mc/game/version_manifest.json'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions


