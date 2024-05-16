#? Api calls to mc-jars backend
import requests



mc_jars_api='http://127.0.0.1:8000/api'

def checkExist(software, version):
  """
  Check if a version of the
  software already exists so we don't build it twice
  """
  pass

def uploadVersion(file, project, stype, version, buildnum = 0):
  params = {
      'project': project,
      'version': version,
      'build': buildnum
  }

  headers = {
      'accept': 'application/json',
  }
  files = {
      'file': (file, open(file, 'rb'), 'application/java-archive')
  }
  response = requests.post(f'{mc_jars_api}/upload/{stype.lower()}', params=params, headers=headers, files=files)
