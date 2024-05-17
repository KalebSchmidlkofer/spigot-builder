import utils 
import requests
from os import path, mkdir
from loguru import logger
from munch import munchify
from shutil import rmtree
from utils import calls
#? Not really a builder, just uses the papermc api to download the jars
#* This file gets Papermc, Folia, Velocity, Travertine, waterfall
paperapi='https://api.papermc.io/v2/projects'


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
    self.build = buildversion.build
    self.data=returndata
    logger.trace(self.data)
    return self.data


  def download(self):
    logger.trace('Downloading:')
    logger.info(f'{self.project}: {self.version}')
    logger.info(f'build: {self.data["build"]}')
    logger.trace(self.data["download"])
    dwnldurl=f'{paperapi}/{self.project}/versions/{self.version}/builds/{self.data["build"]}/downloads/{self.data["download"]}'
    apidwnld=requests.get(
      dwnldurl,
      allow_redirects=True
    )
    logger.trace(f'api url: {dwnldurl}')
    return apidwnld

projectIden={
  'paper': 'Servers',
  'folia': 'Servers',
  'travertine': 'Proxies',
  'waterfall': 'Proxies',
  'velocity': 'Proxies',

}

def build(
  build_path: str = './paperbuilds',
  version= None,
  project= None,
  auto_cleanup:bool = True
  ):
  
  version=utils.loadPlugin(project)  
  paper=getPaper(project)
  regpath=path.join(f'{build_path}')
  for x in version:
    paper.fetchVersions(x)
    downloadContent=paper.download()
    dlpath=path.join(regpath, paper.data['download'])
    if not path.exists(regpath): 
      mkdir(regpath)
    open(dlpath, '+wb').write(downloadContent.content)
    calls.uploadVersion(dlpath, project, projectIden[project], x, paper.build)

  if auto_cleanup:
    rmtree(regpath)

