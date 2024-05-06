import utils 
import asyncio
paperapi='api.papermc.io/v2/projects'

def fetchVersions(project, version):
  projectVersions=f'{paperapi}/{project}/versions/{version}'


def build(build_path: str, version = None):
  if version == None:
    version=utils.loadPlugin()
  else:
    pass

  
