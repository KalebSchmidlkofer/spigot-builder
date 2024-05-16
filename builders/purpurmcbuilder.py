import utils 
import requests
from os import path, mkdir
from loguru import logger
from munch import munchify
from shutil import rmtree
#? Not really a builder, just uses the papermc api to download the jars
#* This file gets purpurmc, purformance
purpurapi='https://api.purpurmc.org/v2'

#* https://api.purpurmc.org/v2/purpur/1.20.1/1991/download
class getPurpur:
  def __init__(self, project):
    self.project = project

  def fetchVersions(self, version):
    self.version=version
    apifetch=requests.get(f'{purpurapi}/{self.project}/{version}')
    jsonapi=munchify(apifetch.json())
    buildversion=jsonapi.builds['latest'] #type: ignore
    self.data=buildversion
    logger.trace(self.data)
    return self.data


  def download(self):
    logger.trace('Downloading:')
    logger.info(f'{self.project}: {self.version}')
    logger.info(f'build: {self.data}')
    dwnldurl=f'{purpurapi}/{self.project}/{self.version}/{self.data}/download'
    apidwnld=requests.get(
      dwnldurl,
      allow_redirects=True
    )
    logger.trace(f'api url: {dwnldurl}')
    return apidwnld


def build(
  build_path: str = './paperbuilds',
  version= None,
  project= None,
  auto_cleanup:bool = True
  ):
  
  version=utils.loadPurpur(project)
  purpur=getPurpur(project)
  for x in version:
    purpur.fetchVersions(x)
    downloadContent=purpur.download()
    regpath=path.join(f'{build_path}')
    dlpath=path.join(regpath, f'{project}-{purpur.version}-{purpur.data}.jar')
    if not path.exists(regpath): 
      mkdir(regpath)
    open(dlpath, '+wb').write(downloadContent.content)
  if auto_cleanup:
    rmtree(regpath)


