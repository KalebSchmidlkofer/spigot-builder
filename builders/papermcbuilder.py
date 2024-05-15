import utils 
import requests
from os import path, mkdir
from loguru import logger
from munch import munchify
from shutil import rmtree
#? Not really a builder, just uses the papermc api to download the jars
#* This file gets Papermc, Folia, Velocity, Travertine, waterfall
paperapi='https://api.papermc.io/v2/projects/'


class getPaper:
  def __init__(self, project):
    self.project = project

  def fetchVersions(self, version):
    self.version=version
    apifetch=requests.get(f'{paperapi}/{self.project}/versions/{version}/builds')
    jsonapi=munchify(apifetch.json())
    buildversion=jsonapi.builds[-1] #type: ignore
    returndata={
      "build": buildversion.build,
      "download": buildversion.downloads.application.name
    }
    self.data=returndata
    logger.trace(self.data)
    return self.data


  def download(self):
    logger.trace('Downloading:')
    logger.trace(f'{self.project}: {self.version}')
    logger.trace()
    logger.trace(self.data["build"])
    logger.trace(self.data["download"])
    dwnldurl=f'{paperapi}/projects/{self.project}/versions/{self.version}/builds/{self.data["build"]}/downloads/{self.data["download"]}'
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
  
  if version == None:
    version=utils.loadPlugin()  
  else:
    pass
  paper=getPaper(project)
  for x in version:
    paper.fetchVersions(x)
    downloadContent=paper.download()
    regpath=path.join(f'{build_path}')
    dlpath=path.join(regpath, paper.data['download'])
    if not path.exists(regpath): 
      mkdir(regpath)
    open(dlpath, '+wb').write(downloadContent.content)
  if auto_cleanup:
    rmtree(regpath)


