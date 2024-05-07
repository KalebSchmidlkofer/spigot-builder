import utils 
import requests
from os import path, mkdir
from loguru import logger
from munch import munchify
#? Not really a builder, just uses the papermc api to download the jars
paperapi='https://api.papermc.io/v2/projects/'


class getPaper:
  def __init__(self):
    pass


  def fetchVersions(self, project, version, build_path="./paperbuild"):
    self.project=project
    self.version=version
    self.build_path=build_path 
    apifetch=requests.get(f'{paperapi}/{project}/versions/{version}/builds')
    jsonapi=munchify(apifetch.json())
    buildversion=jsonapi.builds[-1] #type: ignore
    returndata={
      "build": buildversion.build,
      "download": buildversion.downloads.application.name
    }
    self.data=returndata
    #print(self.data)
    return self.data


  def download(self):
    logger.trace(self.data["build"])
    logger.trace(self.data["download"])
    logger.trace(self.project)
    logger.trace(self.version)
    apidwnld=requests.get(f'{paperapi}/projects/{self.project}/versions/{self.version}/builds/{self.data["build"]}/downloads/{self.data["download"]}', allow_redirects=True)
    logger.trace(f'api url: {paperapi}{self.project}/versions/{self.version}/builds/{self.data["build"]}/downloads/{self.data["download"]}')
    return apidwnld


def build(build_path: str, version = None):
  if version == None:
    version=utils.loadPlugin()  
  else:
    pass
  paper=getPaper()
  for x in version:
    paper.fetchVersions('paper', x)
    downloadContent=paper.download()
    regpath=path.join('./paperbuilds')
    dlpath=path.join(regpath, paper.data['download'])
    if not path.exists(regpath): 
      mkdir(regpath)
    open(dlpath, '+wb').write(downloadContent.content)



