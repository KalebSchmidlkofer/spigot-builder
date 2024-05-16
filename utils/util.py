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
vanilla_api='https://launchermeta.mojang.com/mc/game/version_manifest.json'


def get_papermc_versions(project:str):
  vapi=f'{papermc_api}/{project}'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions

def get_vanilla_versions() -> list: 
  '''Fetches versions for both old_alpha and release'''
  vapi=vanilla_api
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions:list=vdata['versions']
  re_versions:list=[]
  for x in versions:
    if x['type'] == 'release':
      logger.info('passing')
      re_versions.append(x)
    if x['type'] == 'old_alpha':
      re_versions.append(x)
  return re_versions

def get_snapshot_versions():
  vapi=vanilla_api
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions:list=vdata['versions']
  re_versions:list=[]
  for x in versions:
    if  x['type'] == 'snapshot':
      logger.info('passing')
      re_versions.append(x)

  return versions

def get_purpur_versions(project:str) -> list:
  vapi=f'https://api.purpurmc.org/v2/{project}/'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions

def get_bungeecord():
  vapi='https://ci.md-5.net/job/BungeeCord/lastStableBuild/artifact/bootstrap/target/BungeeCord.jar'

