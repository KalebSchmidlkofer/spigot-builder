import utils 
import asyncio
import requests
import json
from loguru import logger
from munch import Munch, munchify

paperapi='https://api.papermc.io/v2/projects/'


class getPaper:
  def __init__(self):
    pass


  def fetchVersions(self, project, version):
    self.project=project
    self.version=version
    apifetch=requests.get(f'{paperapi}/{project}/versions/{version}/builds')
    jsonapi=munchify(apifetch.json())
    buildversion=jsonapi.builds[-1] #type: ignore
    returndata={
      "build": buildversion.build,
      "download": buildversion.downloads.application.name
    }
    self.data=returndata
    #print(self.data)
    return self._download() 


  def _download(self):
    logger.trace(self.data["build"])
    logger.trace(self.data["download"])
    logger.trace(self.project)
    logger.trace(self.version)
    apidwnld=requests.get(f'{paperapi}/projects/{self.project}/versions/{self.version}/builds/{self.data["build"]}/downloads/{self.data["download"]}', allow_redirects=True)
    print(f'{paperapi}{self.project}/versions/{self.version}/builds/{self.data["build"]}/downloads/{self.data["download"]}')
    return apidwnld


def build(build_path: str, version = None):
  

  if version == None:
    version=utils.loadPlugin()  
  else:
    pass
  paper=getPaper()
  for x in version: 
    print(paper.fetchVersions('paper', x))

