#? Api calls
import requests


def checkExist(software, version):
  """
  Check if a version of the
  software already exists so we don't build it twice
  """
  pass

def uploadVersion(software, version, buildnum:None):