import subprocess
import utils

def _version_to_tuple(version_str):
  try:
    return tuple(map(int, version_str.split('.')))
  except ValueError as e:
    print(f'Failed to parse: {version_str}')
    print(f'Use Verbose to view more info')
    return 

def _tuple_to_version(version_tuple):
  return '.'.join(map(str, version_tuple))



def build(build_path: str, version:list = None):
  
  if not version:
    version=utils.get_paper_versions()
    VERSIONS = [_version_to_tuple(versions) for versions in version]
  else:
    VERSIONS = [_version_to_tuple(version)]
  
  for x in VERSIONS:
    version = _tuple_to_version(x)
    print(f'Building Version: {version}')
    if x > (1,17,1):
     subprocess.run(["docker", "run", "--rm", "-v", f"{build_path}:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-17-alpine"])
    elif x == (1,17,1):
      subprocess.run(["docker", "run", "--rm", "-v", f"{build_path}:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-16-alpine"])
    elif x < (1,17,1):
      subprocess.run(["docker", "run", "--rm", "-v", f"{build_path}:/release:z", "-e", f"VERSION={version}", "--name", f"spigot-builder-{version}", "zastrix/spigot-builder:openjdk-8-alpine"])

    #* After building, have to make an api call to the website with the file which is going to be os.path.join(build_path, f'spigot-{version}.jar')