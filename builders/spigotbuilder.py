import subprocess
import utils
from loguru import logger
#? Is this legal?

def _version_to_tuple(version_str):
  try:
    return tuple(map(int, version_str.split('.')))
  except ValueError as e:
    logger.debug(e)
    logger.warning(f'Failed to parse: {version_str}')
    logger.info(f'Use Verbose to view more info')
    pass

def _tuple_to_version(version_tuple):
  return '.'.join(map(str, version_tuple))



def build(build_path: str, version = None):
  
  if version == None:
    version=utils.get_paper_versions()
    VERSIONS = [_version_to_tuple(versions) for versions in version]
  else:
    VERSIONS = [_version_to_tuple(version)]
  
  for x in VERSIONS:
    if x == None:
      pass
    version = _tuple_to_version(x)
    logger.trace(f'Bulding Version: {version}')
    if x > (1,17,1):
     subprocess.run(["docker", "run", "--rm", "-v", f"{build_path}:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-17-alpine"])
    elif x == (1,17,1):
      subprocess.run(["docker", "run", "--rm", "-v", f"{build_path}:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-16-alpine"])
    elif x < (1,17,1):
      subprocess.run(["docker", "run", "--rm", "-v", f"{build_path}:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-8-alpine"])
    logger.trace('Making api call')
    #* After building, have to make an api call to the website with the file which is going to be os.path.join(build_path, f'spigot-{version}.jar')
