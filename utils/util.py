import requests

def get_paper_versions():
  vapi='https://api.papermc.io/v2/projects/paper'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions

def get_vanilla_version(release:bool=False, snapshot:bool=False):
  vapi='https://launchermeta.mojang.com/mc/game/version_manifest.json'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  releaseList=[]
  snapshotList=[]
  for x in versions:
    if x['type'] == 'release':
      releaseList.append(x)
    elif x['type'] == 'snapshot':
      snapshotList.append(x)
  return releaseList, snapshotList

def get_purpur_versions():
  vapi='https://api.purpurmc.org/v2/purpur/'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  if not vdata['project'] == 'purpur':
    raise ValueError
  versions=vdata['versions']
  return versions

def get_bungeecord():
  vapi='https://ci.md-5.net/job/BungeeCord/lastStableBuild/artifact/bootstrap/target/BungeeCord.jar'